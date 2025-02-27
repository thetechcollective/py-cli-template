#!/usr/bin/env python3

#TODO: Change the name of the file to match your command

import os
import sys
import argparse
import re
import pprint

# Add the subdirectory containing the classes to the general class_path
# Import your own classes from the ./classes directory below this line
class_path = os.path.dirname(os.path.abspath(__file__)) + "/classes"
sys.path.append(class_path)

from gitter import Gitter

def parse(args=None):
    global parser
    # Define the parent parser with the --verbose argument
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')

    # Define command-line arguments
    parser = argparse.ArgumentParser(
        prog='gh sample',  #TODO: Change the name of the cli  
        parents=[parent_parser],
        description="""   
            A command-line tool designed to be run as a gh cli extension.  
            """,)  # The description of the command #TODO: Change this to your command description


    # Create alpha, beta and delta subcommands
    subparsers = parser.add_subparsers(dest='command')

    # Add alpha subcommand
    alpha_parser = subparsers.add_parser('alpha', parents=[parent_parser], help='Set the issue number context to work on')
    alpha_group = alpha_parser.add_mutually_exclusive_group()
    alpha_group.add_argument('-i', '--issue', type=int, help='Issue number')
    alpha_group.add_argument('-t', '--title', type=str, help='Title for the new issue')
    assign_group = alpha_parser.add_mutually_exclusive_group()
    assign_group.add_argument('--assign', dest='assignee', action='store_true', help='Assign @me to the issue (default)')
    assign_group.add_argument('--no-assign', dest='assignee', action='store_false', help='Do not assign anybody to the issue')
    alpha_parser.set_defaults(assignee=True, exclusive_groups=['alpha'])    
    
    
    # Add beta subcommand
    beta_parser = subparsers.add_parser('beta', parents=[parent_parser], help='Your description of the alpha subcommand feature')
    beta_parser.add_argument('-m', '--message', type=str, help='Message ...')

    # Add delta subcommand
    delta_parser = subparsers.add_parser(
        'delta', 
        parents=[parent_parser], help='Your description of the alpha subcommand feature',
        description="""
            A multi-line description of the delta subcommand feature.
            Add as much info as needed for the user to feel comfortable using the command. 
            Note that alpha and beta subcommands do not have this description. It's optional.
            """)
    delta_parser.add_argument('--title', type=str, help='Title ...')

    args = parser.parse_args(args)
    return args



if __name__ == "__main__":
    args = parse(sys.argv[1:])
    
    Gitter.verbose(verbose=args.verbose)
    # Gitter.read_cache()
    Gitter.validate_gh_version()
    Gitter.validate_gh_scope(scope='project')
  
    if args.command == 'alpha':
        if args.issue:
            print(f"Subcommand: {args.command}, Issue: {args.issue}, Assignee: {args.assignee}")
            print("Not implemented yet!")
            sys.exit(0)
            
        elif args.title:
            print(f"Subcommand: {args.command}, Title: {args.title}, Assignee: {args.assignee}")
            print("Not implemented yet!")
            sys.exit(0)
          
    if args.command == 'beta':
        print(f"Subcommand: {args.command}, Message: {args.message}")
        print("Not implemented yet!")
        sys.exit(0)
    
    if args.command == 'delta':
        print(f"Subcommand: {args.command}, Title: {args.title}")
        print("Not implemented yet!")
        sys.exit(0)
        
    if args.command is None:
        # Print help if no arguments are provided
        parser.print_help()
        
        
        # Iterate through subparsers and print their help text
        subparsers_actions = [action for action in parser._actions if isinstance(action, argparse._SubParsersAction)]
        for subparsers_action in subparsers_actions:
            for cmd, subparser in subparsers_action.choices.items():
                print("\nHelp for subcommand:", cmd)
                subparser.print_help()        
        sys.exit(0)    
        
    # Gitter.write_cache()          
    exit(0)
