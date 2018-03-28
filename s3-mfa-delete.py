#!/usr/bin/env python

import sys
import click
import boto3


@click.command()
@click.option('--bucket_name', prompt='Bucket name',
              help='Bucket to be configured with MFA delete')
@click.option('--mfa_delete', default='enable',
              type=click.Choice(['enable', 'disable']),
              prompt='MFA delete(enable/disable)?',
              help='Enable or disable MFA Delete')
@click.option('--mfa_serial_number', prompt='MFA serial number',
              help='AWS account id')
@click.option('--mfa_token', prompt='MFA token',
              help='The current token displayed on the MFA device')
def s3_mfa_delete(bucket_name, mfa_serial_number,
                  mfa_delete, mfa_token):
    """Enable versioning on a bucket"""
    s3 = boto3.resource('s3')

    # Create the MFA string for the API call
    # concatenation of the authentication device's serial number,
    # a space, and the value that is displayed on your authentication device
    mfa = '{0} {1}'.format(mfa_serial_number, mfa_token)

    # Get the current status of versioning on the bucket
    # and print the value out.
    bucket_versioning = s3.BucketVersioning(bucket_name)

    if mfa_delete == 'enable':

        if (bucket_versioning.mfa_delete is None or
            bucket_versioning.mfa_delete == 'Disabled'):
            bucket_versioning.put(MFA=mfa,
                                  VersioningConfiguration={
                                     'MFADelete': 'Enabled',
                                     'Status': 'Enabled'
                                  })
            print('\nMFA delete is enabled!')
        else:
            print('\nMFA delete is enabled')

    elif mfa_delete == 'disable':

        if bucket_versioning.mfa_delete == 'Enabled':
            bucket_versioning.put(MFA=mfa,
                                  VersioningConfiguration={
                                    'MFADelete': 'Disabled',
                                    'Status': 'Enabled'
                                  })
            print('\nMFA delete is disabled!')
        else:
            print('\nMFA delete is disabled')

    else:
        print('\nMFA delete value is incorrect')


def main():
    """Main entry point for the script."""
    s3_mfa_delete()


if __name__ == '__main__':
    sys.exit(main())
