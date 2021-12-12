< chessbody >
< !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *-->

< style >
.chesstable
{
    border - style: ridge;
border - width: 0
px;
border - collapse: collapse;

}
.chess - table
{
    background - color: khaki;
box - shadow: 10
px
10
px
5
px
grey;
}
.white - coin
{
    box - sizing: border - box;
background - color: wheat;
width: 50
px;
text - align: center;
height: 50
px;
line - height: 50
px;
font - size: 30
px;
}

.chesstable, th, td
{
    border: 1px solid  # 666;
}
.chesstable
th,.chesstable
td
{
    padding: 10px; / *Apply
cell
padding * /
}
.black - coin
{
    box - sizing: border - box;
background - color: gray;
width: 50
px;
line - height: 50
px;
text - align: center;
height: 50
px;
font - size: 30
px;
}
.chessCoin

{
    border - color: yellow;
border - width: 5
px;
border - style: ridge;
}
.activeChessGrid
{
    border - color: red;
border - width: 5
px;
border - style: ridge;
}
.attackableChessGrid
{
    border - color: yellow;
border - width: 5
px;
border - style: ridge;
}
.currentChessGrid
{
    border - color: lime;
border - width: 5
px;
border - style: ridge;
}
chessbody
{
    background - color: khaki;
}
< / style >
< script >

var
currentCoin = 0;
function
doSelect(event)
{
    uncheckAll();
currentCoin = event.target;
console.log(currentCoin);
event.target.classList.add("currentChessGrid");
console.log(event.target.title);
}
function
getY(id)
{
return Number(id[1]);
}
function
getX(id)
{
return Number(id[2]);
}
function
isPointInRange(y, x)
{
if (y < 1 | | y > 8 | | x < 1 | | x > 8)
    return false;
    return true;
}
function
uncheckAll()
{
for (var i=1;i <= 5;i++)
    {
        var
    x = document.getElementById("h" + i);
    x.classList.remove("currentChessGrid");

    }
    }


    function
    removeAll()
    {
    for (var i=1;i <= 8;i++)
        for (var j=1;j <= 8;j++)
            {
                removeCss(i, j);

            }
            }
            function
            removeCss(y, x)
            {
            if (!isPointInRange(y, x))
            return;
            coin = document.getElementById("a" + y + x);
            coin.innerHTML = "" + y + x;
            coin.classList.remove("activeChessGrid");
            coin.classList.remove("currentChessGrid");
            coin.classList.remove("attackableChessGrid");

            }
            function
            markWithCss(y, x)
            {
            if (!isPointInRange(y, x))
            return;
            coin = document.getElementById("a" + y + x);
            coin.classList.add("activeChessGrid");
            }

            function
            bishopsMap(y, x)
            {
            var
            total = y + x;
            for (var row=1;row <= 8;row++)
                {
                    var
                py = row;
                var
                px = total - row;
                markWithCss(py, px);
                }

                diff = y - x;
                for (var row=1;row <= 8;row++)
                    {
                        var
                    py = row;
                    var
                    px = row - diff;
                    markWithCss(py, px);
                    }
                    }

                    function
                    rooksMap(y, x)
                    {
                    var
                    total = y + x;
                    for (var row=1;row <= 8;row++)
                        {

                            markWithCss(y, row);
                        markWithCss(row, x);
                        }

                        }

                        function
                        queensMap(y, x)
                        {
                        rooksMap(y, x);
                        bishopsMap(y, x);
                        }



                        function
                        kingsMap(y, x)
                        {
                        markWithCss(y + 1, x + 1);
                        markWithCss(y + 1, x - 1);
                        markWithCss(y - 1, x + 1);
                        markWithCss(y - 1, x - 1);
                        markWithCss(y + 1, x);
                        markWithCss(y - 1, x);
                        markWithCss(y, x + 1);
                        markWithCss(y, x - 1);
                        }


                        function
                        pawnsMap(y, x)
                        {
                        markWithCss(y - 1, x);
                        if (isPointInRange(y - 1, x - 1))
                            {
                                var
                            coin = document.getElementById("a" + (y - 1) + (x - 1));
                            coin.classList.add("attackableChessGrid");
                            }
                            if (isPointInRange(y - 1, x + 1))
                                {
                                    var
                                coin = document.getElementById("a" + (y - 1) + (x + 1));
                                coin.classList.add("attackableChessGrid");

                                }
                                if (y == 8)
                                    markWithCss(y - 2, x);
                                }

                                function
                                knightsMap(y, x)
                                {
                                markWithCss(y + 1, x + 2);
                                markWithCss(y + 1, x - 2);
                                markWithCss(y - 1, x + 2);
                                markWithCss(y - 1, x - 2);
                                markWithCss(y + 2, x + 1);
                                markWithCss(y + 2, x - 1);
                                markWithCss(y - 2, x + 1);
                                markWithCss(y - 2, x - 1);
                                }
                                function
                                doProcess(event)
                                {
                                if (currentCoin == 0)
                                    {
                                        alert("Please select a coin");
                                return;
                                }
                                removeAll();
                                // alert(event.target.id);
                                // alert(event.target.parentNode);
                                event.target.classList.add("currentChessGrid");
                                event.target.innerHTML = currentCoin.innerHTML;
                                var
                                y = getY(event.target.id);
                                var
                                x = getX(event.target.id);
                                console.log(y + "," + x);
                                if (currentCoin.title == "Knight")
                                knightsMap(y, x);
                                if (currentCoin.title == "Bishop")
                                bishopsMap(y, x);
                                if (currentCoin.title == "Rook")
                                rooksMap(y, x);
                                if (currentCoin.title == "Queen")
                                queensMap(y, x);
                                if (currentCoin.title == "King")
                                kingsMap(y, x);
                                if (currentCoin.title == "Pawn")
                                pawnsMap(y, x);
                                }
                                < / script >

                                < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * -->
                                < div style="overflow: scroll;" >
                                < center >
                                < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** --> < table


                                class ="chess-table chesstable" style="height: 400px; width: 600px;" >

                                < tbody > < tr >
                                < td > < div


                                class ="white-coin" id="a11" onclick="doProcess(event)" > 11 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a12" onclick="doProcess(event)" > 12 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a13" onclick="doProcess(event)" > 13 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a14" onclick="doProcess(event)" > 14 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a15" onclick="doProcess(event)" > 15 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a16" onclick="doProcess(event)" > 16 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a17" onclick="doProcess(event)" > 17 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a18" onclick="doProcess(event)" > 18 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < div


                                class ="black-coin" id="a21" onclick="doProcess(event)" > 21 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a22" onclick="doProcess(event)" > 22 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a23" onclick="doProcess(event)" > 23 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a24" onclick="doProcess(event)" > 24 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a25" onclick="doProcess(event)" > 25 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a26" onclick="doProcess(event)" > 26 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a27" onclick="doProcess(event)" > 27 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a28" onclick="doProcess(event)" > 28 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < div


                                class ="white-coin" id="a31" onclick="doProcess(event)" > 31 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a32" onclick="doProcess(event)" > 32 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a33" onclick="doProcess(event)" > 33 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a34" onclick="doProcess(event)" > 34 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a35" onclick="doProcess(event)" > 35 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a36" onclick="doProcess(event)" > 36 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a37" onclick="doProcess(event)" > 37 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a38" onclick="doProcess(event)" > 38 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < div


                                class ="black-coin" id="a41" onclick="doProcess(event)" > 41 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a42" onclick="doProcess(event)" > 42 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a43" onclick="doProcess(event)" > 43 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a44" onclick="doProcess(event)" > 44 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a45" onclick="doProcess(event)" > 45 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a46" onclick="doProcess(event)" > 46 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a47" onclick="doProcess(event)" > 47 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a48" onclick="doProcess(event)" > 48 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < div


                                class ="white-coin" id="a51" onclick="doProcess(event)" > 51 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a52" onclick="doProcess(event)" > 52 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a53" onclick="doProcess(event)" > 53 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a54" onclick="doProcess(event)" > 54 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a55" onclick="doProcess(event)" > 55 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a56" onclick="doProcess(event)" > 56 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a57" onclick="doProcess(event)" > 57 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a58" onclick="doProcess(event)" > 58 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < div


                                class ="black-coin" id="a61" onclick="doProcess(event)" > 61 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a62" onclick="doProcess(event)" > 62 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a63" onclick="doProcess(event)" > 63 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a64" onclick="doProcess(event)" > 64 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a65" onclick="doProcess(event)" > 65 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a66" onclick="doProcess(event)" > 66 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a67" onclick="doProcess(event)" > 67 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a68" onclick="doProcess(event)" > 68 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < div


                                class ="white-coin" id="a71" onclick="doProcess(event)" > 71 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a72" onclick="doProcess(event)" > 72 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a73" onclick="doProcess(event)" > 73 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a74" onclick="doProcess(event)" > 74 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a75" onclick="doProcess(event)" > 75 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a76" onclick="doProcess(event)" > 76 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a77" onclick="doProcess(event)" > 77 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a78" onclick="doProcess(event)" > 78 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < div


                                class ="black-coin" id="a81" onclick="doProcess(event)" > 81 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a82" onclick="doProcess(event)" > 82 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a83" onclick="doProcess(event)" > 83 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a84" onclick="doProcess(event)" > 84 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a85" onclick="doProcess(event)" > 85 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a86" onclick="doProcess(event)" > 86 < / div > < / td >

                                < td > < div


                                class ="black-coin" id="a87" onclick="doProcess(event)" > 87 < / div > < / td >

                                < td > < div


                                class ="white-coin" id="a88" onclick="doProcess(event)" > 88 < / div > < / td >

                                < / tr >

                                < tr >
                                < td > < h1 > < / h1 > < / td >
                                < td > < h1


                                class ="chessCoin" id="h1" onclick="doSelect(event)" style="box-shadow: grey 10px 10px 5px; height: 50px; line-height: 50px; text-align: center; width: 50px;" title="Rook" > ♜ < / h1 > < / td >

                                < td > < h1


                                class ="chessCoin" id="h2" onclick="doSelect(event)" style="box-shadow: grey 10px 10px 5px; height: 50px; line-height: 50px; text-align: center; width: 50px;" title="Knight" > ♞ < / h1 > < / td >

                                < td > < h1


                                class ="chessCoin" id="h3" onclick="doSelect(event)" style="box-shadow: grey 10px 10px 5px; height: 50px; line-height: 50px; text-align: center; width: 50px;" title="Bishop" > ♝ < / h1 > < / td >

                                < td > < h1


                                class ="chessCoin" id="h4" onclick="doSelect(event)" style="box-shadow: grey 10px 10px 5px; height: 50px; line-height: 50px; text-align: center; width: 50px;" title="Queen" > ♛ < / h1 > < / td >

                                < td > < h1


                                class ="chessCoin" id="h5" onclick="doSelect(event)" style="box-shadow: grey 10px 10px 5px; height: 50px; line-height: 50px; text-align: center; width: 50px;" title="King" > ♚ < / h1 > < / td >

                                < td > < h1


                                class ="chessCoin" id="h6" onclick="doSelect(event)" style="box-shadow: grey 10px 10px 5px; height: 50px; line-height: 50px; text-align: center; width: 50px;" title="Pawn" > ♟ < / h1 > < / td >

                                < td > < h1 > < / h1 > < / td >

                                < / tr >
                                < / tbody > < / table >
                                < / center >
                                < / div >
                                < !-- ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** -->
                                < script >
                                function
                                chessOnStart()
                                {
                                    var
                                x = document.getElementById("h6");
                                x.scrollIntoView();

                                }
                                chessOnStart();

                                < / script >
                                < / chessbody >
