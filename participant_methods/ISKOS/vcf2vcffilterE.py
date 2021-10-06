#!/usr/bin/env python3
'''
--------------------------------------------------------------------------------

vcf2vcffilter.py: Script that adds a FILTER flag to variants in VCF1 that are\
 not present in VCF2

--------------------------------------------------------------------------------
'''

import argparse
import datetime
import pysam
import sys


__version__ = '1.0.0'


def add_filter_flag_to_vcf(options):
    small_vcf = pysam.VariantFile(options.secondVcf)
    small_list = {}
    for small_rec in small_vcf.fetch():
        schr = str(small_rec.chrom)
        spos = str(small_rec.pos)
        sref = str(small_rec.ref)
        for alt_allele in small_rec.alts:
            tmp_key = '_'.join((schr, spos, sref, alt_allele))
            small_list[tmp_key] = 1

    vcf_in = pysam.VariantFile(options.mainVcf)
    vcf_in.header.add_meta(
        key='FILTER',
            items=(('ID', options.flagName),
                   ('Description', options.flagDescription)))

    vcf_out = pysam.VariantFile(options.vcfOut, 'w', header=vcf_in.header)

    prev_chr = 'chr0'
    for rec in vcf_in.fetch():
        ti = datetime.datetime.now()
        to_be_flagged = False
        chr = str(rec.chrom)
        if chr != prev_chr:
            nvar = 0
        nvar += 1
        pos = str(rec.pos)
        ref = str(rec.ref)
        for alt_allele in rec.alts:
            vcf_key = '_'.join((chr, pos, ref, alt_allele))
            if vcf_key not in small_list.keys():
                to_be_flagged = True
        if to_be_flagged is True:
            if options.deleteExistingFilters is True:
                rec.filter.clear()
            rec.filter.add(options.flagName)
        else:
            rec.filter.clear()
            rec.filter.add('PASS')

        vcf_out.write(rec)
        tf = datetime.datetime.now()
        time_in_seconds = time_diff(ti, tf)
        print('\t'.join((chr, str(nvar), str(time_in_seconds))))
        prev_chr = chr

    if options.vcfOut != '-':
        vcf_out.close()
        pysam.tabix_index(options.vcfOut, preset='vcf', force=True)


def get_v2vf_options(argv):
    v2vf_parser = argparse.ArgumentParser(
        usage='''vcf2vcffilter.py [options]

Script that adds a FILTER flag to variants in VCF1 that are not present in VCF2
'''
    )
    v2vf_parser.add_argument(
        '--mainVcf',
        '-V1',
        required=True,
        help="FILE Main vcf input file",
    )
    v2vf_parser.add_argument(
        '--secondVcf',
        '-V2',
        required=True,
        help="FILE Second vcf input file",
    )
    v2vf_parser.add_argument(
        '--flagName',
        '-F',
        required=True,
        help="STR Flag tag",
    )
    v2vf_parser.add_argument(
        '--flagDescription',
        '-D',
        default='Default flag',
        help="STR Description to be added in the output vcf header",
    )
    v2vf_parser.add_argument(
        '--vcfOut',
        '-O',
        default='-',
        help="FILE Output vcf file",
    )
    v2vf_parser.add_argument(
        '--deleteExistingFilters',
        '-def',
        action='store_true',
        default=False,
        help="Bool Delete existing filters",
    )
    
    return v2vf_parser.parse_args(argv)


def no_flags():
    print('Please re-run the command with "-h" to get usage instructions\
 and a complete list of options\n')
    exit()


def validate_options(options):
    pass


def time_diff(t0,t1):
    delta_time = datetime.timedelta.total_seconds(t1-t0)
    return(format(delta_time, '.6f'))


def main():
    if len(sys.argv) == 1:
        no_flags()
    else:
        v2vf_opts = get_v2vf_options(sys.argv[1:])
        validate_options(v2vf_opts)
        add_filter_flag_to_vcf(v2vf_opts)
        exit(0)


if __name__ == '__main__':
    exit(main())
