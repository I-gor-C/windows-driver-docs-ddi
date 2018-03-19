---
UID: NE:ksmedia.TELEPHONY_CALLTYPE
title: TELEPHONY_CALLTYPE
author: windows-driver-content
description: The TELEPHONY_CALLTYPE enumeration defines constants that specify the type of phone call.
old-location: audio\telephony_calltype.htm
old-project: audio
ms.assetid: 8CF2CAF2-29F2-4B8B-B23F-B423392B2DAF
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: TELEPHONY_CALLTYPE, TELEPHONY_CALLTYPE enumeration [Audio Devices], TELEPHONY_CALLTYPE_CIRCUITSWITCHED, TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE, TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN, audio.telephony_calltype, ksmedia/TELEPHONY_CALLTYPE, ksmedia/TELEPHONY_CALLTYPE_CIRCUITSWITCHED, ksmedia/TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE, ksmedia/TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: None supported
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ksmedia.h
api_name:
-	TELEPHONY_CALLTYPE
product: Windows
targetos: Windows
req.typenames: TELEPHONY_CALLTYPE
---

# TELEPHONY_CALLTYPE Enumeration
The <b>TELEPHONY_CALLTYPE</b> enumeration defines constants that specify the type of phone call.

## Syntax
````
typedef enum  { 
  TELEPHONY_CALLTYPE_CIRCUITSWITCHED      = 0,
  TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE   = 1,
  TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN  = 2
} TELEPHONY_CALLTYPE;
````

## Constants

<table>
            
                <tr>
                    <td>TELEPHONY_CALLTYPE_CIRCUITSWITCHED</td>
                    <td>Specifies a circuit-switched phone call.</td>
                </tr>
            
                <tr>
                    <td>TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE</td>
                    <td>Specifies a packet-switched Long-Term Evolution (LTE) phone call.</td>
                </tr>
            
                <tr>
                    <td>TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN</td>
                    <td>Specifies a packet-switched wireless LAN (WLAN) phone call.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10,Windows 10 Mobile Windows 10,Windows 10 Mobile |
| **Header** | ksmedia.h |

## See Also

<a href="..\ksmedia\ns-ksmedia-_tagkstelephony_providerchange.md">KSTELEPHONY_PROVIDERCHANGE</a>



<a href="..\ksmedia\ns-ksmedia-_tagkstelephony_callcontrol.md">KSTELEPHONY_CALLCONTROL</a>



<a href="..\ksmedia\ns-ksmedia-_tagkstelephony_callinfo.md">KSTELEPHONY_CALLINFO</a>