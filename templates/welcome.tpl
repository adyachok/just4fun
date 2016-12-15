<html>
    <head>
       <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">

        <script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
        <script src="https://npmcdn.com/tether@1.2.4/dist/js/tether.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js"></script>

        <link href="/static/main.css" rel="stylesheet">
        <script src="/static/main.js"></script>
    </head>
    <body>
        <div class="container-fluid">
            <div>
                <h2>Presentations</h2>
                <div class="row">
                    <div class="col-md-4 col-md-offset-4">
                        <form>
                            <input id="presentationSearch" class="form-control form-control-lg" type="text" placeholder="Enter presentation title" />
                        </form>
                    </div>
                </div>

                <table id="presentations" class="table table-striped">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Thumbnail</th>
                        <th>Title</th>
                        <th>Creator</th>
                        <th>Creation date <span id="sortPoint" class="glyphicon glyphicon-arrow-down" aria-hidden="true" style="cursor:pointer;"></span></th>
                    </tr>
                    </thead>
                    <tbody>
                    </tbody>
                </table>
            </div>
        </div>

        <script type="text/javascript">
            $(document).ready(init);
        </script>
    </body>
</html>