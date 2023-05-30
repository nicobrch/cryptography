// ==UserScript==
// @name         Lab Criptografia
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  try to take over the world!
// @author       Nico
// @match        https://cripto.tiiny.site/
// @grant        none
// ==/UserScript==

function getTextInParagraphByClass(className) {
    var divElement = document.querySelector('div.' + className);
    if (divElement) {
        var paragraphElement = divElement.querySelector('p');
        if (paragraphElement) {
            return paragraphElement.textContent;
        }
    }
    return '';
}

function extractFirstLetters(text) {
    var sentences = text.split('.');
    var cleanedSentences = sentences.map(function(sentence) {
        return sentence.trim();
    });
    var firstLetters = cleanedSentences.map(function(sentence) {
        return sentence.charAt(0);
    });
    var result = firstLetters.join('');
    return result;
}

function getDivIdsWithClassMX() {
    var divs = Array.from(document.getElementsByTagName('div'));
    var idValues = divs
        .filter(function(div) {
            return div.className.includes('M');
        })
        .map(function(div) {
            return div.id;
        });
    return idValues;
}

function decryptMessages(encodedMessages, llave) {
    var key = CryptoJS.enc.Utf8.parse(llave);
    var decryptedMessages = encodedMessages.map(function(encodedMessage) {
        var ciphertext = CryptoJS.enc.Base64.parse(encodedMessage);
        var decrypted = CryptoJS.TripleDES.decrypt(
            { ciphertext: ciphertext },
            key,
            { mode: CryptoJS.mode.ECB }
        );
        var decryptedText = decrypted.toString(CryptoJS.enc.Utf8);
        return decryptedText;
    });
    return decryptedMessages;
}

function createParagraph(text) {
    var paragraphElement = document.createElement('p');
    paragraphElement.textContent = text;
    document.body.appendChild(paragraphElement);
}

function addDivElement(id, className) {
    var divElement = document.createElement('div');
    divElement.className = className;
    divElement.id = id;
    divElement.textContent = ' ';
    document.body.appendChild(divElement);
}

(function() {
    'use strict';

    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js';
    script.integrity = 'sha512-nOQuvD9nKirvxDdvQ9OMqe2dgapbPB7vYAMrzJihw5m+aNcf0dX53m6YxM4LgA9u8e9eg9QX+/+mPu8kCNpV2A==';
    script.crossOrigin = 'anonymous';

    script.onload = function() {
        addDivElement('4PRw0NDwUiE=', 'M8');
        addDivElement('Y/swZiYABWw=', 'M9');
        addDivElement('JqCvMff/Gwg=', 'M10');
        addDivElement('gBHMtVf+IxY=', 'M11');

        var texto = getTextInParagraphByClass('Parrafo');
        var llave = extractFirstLetters(texto);
        var cifrados = getDivIdsWithClassMX();
        var descifrados = decryptMessages(cifrados, llave);

        descifrados.map(function(value) {
            createParagraph(value);
        });

        console.log("La llave es: " + llave);
        console.log("Los mensajes cifrados son: " + cifrados.length);
        console.log("Los mensajes descifrados son: " + descifrados);
        for (var i=0; i<cifrados.length; i++){
            console.log(cifrados[i] + " " + descifrados[i]);
        }
    };

    document.head.appendChild(script);

})();
