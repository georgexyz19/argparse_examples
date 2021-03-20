import click

@click.command()
@click.option('--xhtml', 
              '-x', 
              default=False, 
              help='create a XHTML template instead of HTML')
@click.option('--cssfile', 
              '-c', 
              default='style.css',
              help="CSS file to link")
@click.argument('file')
def main(xhtml, cssfile, file):
    print("xhtml option is: \n    ", xhtml)
    print("cssfile option is : \n    ", cssfile)
    print("file is : \n    ", file)

if __name__ == '__main__':
    main()
