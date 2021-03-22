div.sib-sms-field {
    display: inline-block;
    position: relative;
    width: 100%;
}

.sib-sms-field .sib-country-block {
    position: absolute;
    right: auto;
    left: 0;
    top: 0;
    bottom: 0;
    padding: 1px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

.sib-country-block .sib-toggle.sib-country-flg {
    z-index: 1;
    position: relative;
    width: 46px;
    height: 100%;
    padding: 0 0 0 8px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    background-color: #dbdbdb;
    cursor: pointer;
}

.sib-country-block .sib-toggle .sib-cflags {
    position: absolute;
    top: 0;
    bottom: 0;
    margin: auto;
    height: 15px;
    width: 20px;
    background-repeat: no-repeat;
    background-color: #dbdbdb;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    background-image: url('../img/flags/fr.png');
}
.sib-country-block .sib-toggle .sib-icon-arrow {
    position: absolute;
    top: 50%;
    margin-top: -2px;
    right: 6px;
    width:  0;
    height: 0;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-top: 4px solid;
}
.sib-sms-field ul.sib-country-list {
    position: absolute;
    z-index: 2;
    list-style: none;
    text-align: left;
    padding: 0px;
    margin: 0px 0px 0px -1px;
    box-shadow: rgba(0, 0, 0, 0.2) 1px 1px 4px;
    background-color: white;
    border: 1px solid rgb(204, 204, 204);
    white-space: nowrap;
    max-height: 150px;
    overflow-y: scroll;
    overflow-x: hidden;
    top: 50px;
    width: 250px;
}
.sib-sms-field ul.sib-country-list li.sib-country-prefix {
    font-size: 14px;
    padding:1px 10px;
    cursor: pointer;
}
.sib-sms-field ul.sib-country-list li.sib-country-prefix:hover {
    background-color: #dbdbdb;
}
.sib-sms-field ul.sib-country-list li .sib-flag-box {
    width: 20px;
}

.sib-sms-field ul.sib-country-list li .sib-flag-box .sib-flag {
    height: 18px;
    width: 20px;
    background-image: url("../img/flags/ad.png");
    vertical-align: middle;
    display: inline-block;
    background-repeat:no-repeat;
}
.sib-sms-field ul.sib-country-list li .sib-flag-box .sib-dial-code {
    margin-left: 20px;
}
.sib-sms-field .sib-sms {
    padding-right: 6px;
    padding-left: 52px;
    margin-left: 0;
    position: relative;
    z-index: 0;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
    margin-right: 0;
}
.sib-multi-lists.sib_error {
    color: #A94442;
}