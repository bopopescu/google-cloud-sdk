# Copyright 2013 Google Inc. All Rights Reserved.

"""Provide commands for working with backups of Cloud SQL instances."""


from googlecloudsdk.calliope import base


class BackupRuns(base.Group):
  """Provide commands for working with backups of Cloud SQL instances.

  Provide commands for working with backups of Cloud SQL instances
  including listing and getting information about backups for a Cloud SQL
  instance.
  """

  @staticmethod
  def Args(parser):
    """Args is called by calliope to gather arguments for this command.

    Args:
      parser: An argparse parser that you can use it to add arguments that go
          on the command line after this command. Positional arguments are
          allowed.
    """
    parser.add_argument(
        '--instance',
        '-i',
        required=True,
        help='Cloud SQL instance ID.')
