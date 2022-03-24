def getHTML(row):
    return """
    <!DOCTYPE html PUBLIC>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

        <style>
            body {
                font-family: Tahoma, Geneva, sans-serif;
            }

            h2 {
                text-align: center;
            }

            .chart {
                position: relative;
                width: 500px;
                height: 250px;
            }

            .hold {
                position: absolute;
                width: 200px;
                height: 200px;
                clip: rect(0px, 200px, 200px, 100px);
                top:15px;
                left: 270px;
            }

            .pie {
                position: absolute;
                /*	width:100px;
                    height:200px;
                    -moz-border-radius:100px 0 0 100px;
                    -webkit-border-radius:100px 0 0 100px; 
                    border-radius:100px 0 0 100px;
                    -moz-transform-origin:right center;
                    -webkit-transform-origin:right center;
                    transform-origin:right center; */
                width: 200px;
                height: 200px;
                clip: rect(0px, 100px, 200px, 0px);
                -moz-border-radius: 100px;
                -webkit-border-radius: 100px;
                border-radius: 100px;
            }

            .hold.gt50 {
                clip: rect(auto, auto, auto, auto);
            }

            .pie.fill {
                -moz-transform: rotate(180deg) !important;
                -webkit-transform: rotate(180deg) !important;
                -o-transform: rotate(180deg) !important;
                transform: rotate(180deg) !important;
            }

            .legend {
                clear: left;
                float: left;
                margin-left: 30px;
                margin-top: 15px;
                font-size: 12px;
                border: 2px solid grey;
                border-radius:8px;
                padding: 9px;
                width: 200px;
            }

            .legend DIV {
                margin: 5px 0;
            }

            .legend span {
                float: right;
                padding-left: .3em;
            }

            #browse-FF {
                margin-left: 5px;
                margin-top: -5px;
            }

            #browse-FF .pie {
                background-color: rgb(111, 221, 255);
                border-color: rgb(140, 228, 255);
                -moz-transform: rotate(116.28deg);
                -webkit-transform: rotate(116.28deg);
                -o-transform: rotate(116.28deg);
                transform: rotate(116.28deg);
            }

            #browse-FF-lbl {
                border-left: rgb(25, 201, 255) solid 1em;
                padding-left: .5em;
            }

            #browse-IE {
                -moz-transform: rotate(116.28deg);
                -webkit-transform: rotate(116.28deg);
                -o-transform: rotate(116.28deg);
                transform: rotate(116.28deg);
            }

            #browse-IE .pie {
                background-color: rgb(179, 104, 69);
                border-color: rgb(168, 94, 59);
                -moz-transform: rotate(109.8deg);
                -webkit-transform: rotate(109.8deg);
                -o-transform: rotate(109.8deg);
                transform: rotate(109.8deg);
            }

            #browse-IE-lbl {
                border-left: rgb(172, 98, 64) solid 1em;
                padding-left: .5em;
            }

            #browse-Safari {
                -moz-transform: rotate(226.08deg);
                -webkit-transform: rotate(226.08deg);
                -o-transform: rotate(226.08deg);
                transform: rotate(226.08deg);
            }

            #browse-Safari .pie {
                background-color: rgb(247, 223, 118);
                border-color: rgb(247, 223, 118);
                -moz-transform: rotate(10.08deg);
                -webkit-transform: rotate(10.08deg);
                -o-transform: rotate(10.08deg);
                transform: rotate(10.08deg);
            }

            #browse-Safari-lbl {
                border-left: rgb(247, 223, 118) solid 1em;
                padding-left: .5em;
            }

            #browse-Chrome {
                -moz-transform: rotate(236.16deg);
                -webkit-transform: rotate(236.16deg);
                -o-transform: rotate(236.16deg);
                transform: rotate(236.16deg);
            }

            #browse-Chrome .pie {
                background-color: rgb(101, 255, 121);
                border-color: rgb(101, 255, 121);
                -moz-transform: rotate(62.12deg);
                -webkit-transform: rotate(62.12deg);
                -o-transform: rotate(62.12deg);
                transform: rotate(62.12deg);
            }

            #browse-Chrome-lbl {
                border-left: rgb(101, 255, 121) solid 1em;
                padding-left: .5em;
            }

            #browse-Other {
                -moz-transform: rotate(300.28deg);
                -webkit-transform: rotate(300.28deg);
                -o-transform: rotate(300.28deg);
                transform: rotate(300.28deg);
            }

            #browse-Other .pie {
                background-color: salmon;
                border-color: salmon;
                -moz-transform: rotate(60.76deg);
                -webkit-transform: rotate(60.76deg);
                -o-transform: rotate(60.76deg);
                transform: rotate(60.76deg);
            }

            #browse-Other-lbl {
                border-left: salmon solid 1em;
                padding-left: .5em;
            }



        </style>
    </head>

    <body>
        <div class="chart">
            <div class="legend">
                <h2> """ + row["NAME"] + """</h2>
                <div id="browse-FF-lbl">Fish<span>42.3%</span></div>

                <div id="browse-IE-lbl">Meat<span>30.5%</span></div>
                <div id="browse-Safari-lbl">Cereal<span>2.8%</span></div>
                <div id="browse-Chrome-lbl">Vegetables<span>1.7%</span></div>
                <div id="browse-Other-lbl">Fruits<span>1.6%</span></div>

            </div>
            <div id="browse-IE" class="hold">
                <div class="pie"></div>
            </div>
            <div id="browse-FF" class="hold">
                <div class="pie"></div>
            </div>
            <div id="browse-Safari" class="hold">
                <div class="pie"></div>

            </div>
            <div id="browse-Chrome" class="hold">
                <div class="pie"></div>
            </div>
            <div id="browse-Other" class="hold">
                <div class="pie"></div>
            </div>

            </div>
        </div>

    </body>

    </html>


                    """
