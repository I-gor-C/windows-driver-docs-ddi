---
UID: NE:wditypes._WDI_AUTH_ALGORITHM
title: "_WDI_AUTH_ALGORITHM"
author: windows-driver-content
description: The WDI_AUTH_ALGORITHM enumeration defines the authentication algorithm values.
old-location: netvista\wdi_auth_algorithm.htm
old-project: netvista
ms.assetid: B908A174-F977-484E-A086-6C8C9A914D6C
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: wditypes/WDI_AUTH_ALGORITHM, WDI_AUTH_ALGO_WPA, WDI_AUTH_ALGO_IHV_START, WDI_AUTH_ALGO_80211_SHARED_KEY, WDI_AUTH_ALGO_RSNA_PSK, WDI_AUTH_ALGO_IHV_END, wditypes/WDI_AUTH_ALGO_RSNA_PSK, wditypes/WDI_AUTH_ALGO_80211_OPEN, netvista.wdi_auth_algorithm, wditypes/WDI_AUTH_ALGO_80211_SHARED_KEY, wditypes/WDI_AUTH_ALGO_IHV_END, WDI_AUTH_ALGO_80211_OPEN, wditypes/WDI_AUTH_ALGO_WPA_NONE, _WDI_AUTH_ALGORITHM, wditypes/WDI_AUTH_ALGO_WPA, WDI_AUTH_ALGO_WPA_PSK, WDI_AUTH_ALGO_RSNA, WDI_AUTH_ALGORITHM, netvista.wifi_auth_algorithm, wditypes/WDI_AUTH_ALGO_IHV_START, WDI_AUTH_ALGORITHM enumeration [Device and Driver Installation], wditypes/WDI_AUTH_ALGO_RSNA, WDI_AUTH_ALGO_WPA_NONE, wditypes/WDI_AUTH_ALGO_WPA_PSK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wditypes.hpp
apiname:
-	WDI_AUTH_ALGORITHM
product: Windows
targetos: Windows
req.typenames: WDI_AUTH_ALGORITHM
req.product: Windows 10 or later.
---

# _WDI_AUTH_ALGORITHM Enumeration
The WDI_AUTH_ALGORITHM enumeration defines the authentication algorithm values.

## Syntax
````
typedef enum _WDI_AUTH_ALGORITHM { 
  WDI_AUTH_ALGO_80211_OPEN        = 1,
  WDI_AUTH_ALGO_80211_SHARED_KEY  = 2,
  WDI_AUTH_ALGO_WPA               = 3,
  WDI_AUTH_ALGO_WPA_PSK           = 4,
  WDI_AUTH_ALGO_WPA_NONE          = 5,
  WDI_AUTH_ALGO_RSNA              = 6,
  WDI_AUTH_ALGO_RSNA_PSK          = 7,
  WDI_AUTH_ALGO_IHV_START         = 0x80000000,
  WDI_AUTH_ALGO_IHV_END           = 0xffffffff
} WDI_AUTH_ALGORITHM;
````

## Constants

<table>
            
                <tr>
                    <td>WDI_AUTH_ALGO_80211_OPEN</td>
                    <td>Specifies an IEEE 802.11 Open System authentication algorithm.</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_80211_SHARED_KEY</td>
                    <td>Specifies an IEEE 802.11 Shared Key authentication algorithm that requires the use of a pre-shared Wired Equivalent Privacy (WEP) key for the 802.11 authentication.</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_IHV_END</td>
                    <td>Specifies the end of the range that specifies proprietary authentication algorithms that are developed by an IHV.</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_IHV_START</td>
                    <td>Specifies the start of the range that specifies proprietary authentication algorithms that are developed by an IHV.</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_RSNA</td>
                    <td>Specifies an IEEE 802.11i Robust Security Network Association (RSNA) algorithm. IEEE 802.1X port authorization is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process. 

When the RSNA algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the Robust Security Network (RSN) IE.</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_RSNA_PSK</td>
                    <td>Specifies an IEEE 802.11i RSNA algorithm that uses PSK. IEEE 802.1X port authorization is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a pre-shared key that is used on both the supplicant and authenticator. 

When the RSNA PSK algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 2 (preshared key) within the RSN IE.</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_WPA</td>
                    <td>Specifies a Wi-Fi Protected Access (WPA) algorithm. IEEE 802.1X port authorization is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process. 

When the WPA algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the WPA information element (IE).</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_WPA_NONE</td>
                    <td>This value is not supported.</td>
                </tr>
            
                <tr>
                    <td>WDI_AUTH_ALGO_WPA_PSK</td>
                    <td>Specifies a Wi-Fi Protected Access (WPA) algorithm that uses preshared keys (PSK). IEEE 802.1X port authorization is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a preshared key that is used on both the supplicant and authenticator. 

When the WPA PSK algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 2 (preshared key) within the WPA IE.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | wditypes.hpp |