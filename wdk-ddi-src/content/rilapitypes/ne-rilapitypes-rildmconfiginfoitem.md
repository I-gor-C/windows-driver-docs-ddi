---
UID : NE:rilapitypes.RILDMCONFIGINFOITEM
title : RILDMCONFIGINFOITEM
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rildmconfiginfoitem_2.htm
old-project : netvista
ms.assetid : b7239fae-253c-4ac9-ba96-8e10cce5598d
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILDMCONFIGINFOITEM, RILDMCONFIGINFOITEM
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILDMCONFIGINFOITEM
req.alt-loc : rilapitypes.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : RILDMCONFIGINFOITEM
req.product : Windows 10 or later.
---

# RILDMCONFIGINFOITEM Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILDMCONFIGINFOITEM { 
  RILDMCONFIG_SIP_TIMER_T2,
  RILDMCONFIG_SIP_TIMER_F,
  RILDMCONFIG_SMS_FORMAT_TYPE,
  RILDMCONFIG_DOMAIN_NAME,
  RILDMCONFIG_SMS_OVER_IP_NW_INDICATION,
  RILDMCONFIG_IMS_TEST_MODE_STATUS,
  RILDMCONFIG_PCSCF_ADDRESS,
  RILDMCONFIG_PCSCF_PORT_NUMBER,
  RILDMCONFIG_MD5_AUTH,
  RILDMCONFIG_MULTIPARTY_SERVER,
  RILDMCONFIG_REQUEST_CONTEXT,
  RILDMCONFIG_IMS_NAI,
  RILDMCONFIG_SIP_SESSION_TIMER,
  RILDMCONFIG_SIP_SESSION_TIMER_MIN,
  RILDMCONFIG_AMR_WB_ENABLE,
  RILDMCONFIG_AMR_SRC_CTL_RATE,
  RILDMCONFIG_AMR_WB_SRC_CTL_RATE,
  RILDMCONFIG_AMR_MODE_SET,
  RILDMCONFIG_AMR_WB_MODE_SET,
  RILDMCONFIG_RINGING_TIMER,
  RILDMCONFIG_RINGBACK_TIMER,
  RILDMCONFIG_RTC_INACTIVITY_TIMER,
  RILDMCONFIG_UDP_KEEPALIVE_TIMER,
  RILDMCONFIG_IMS_VOICE_ENABLED,
  RILDMCONFIG_IMS_VIDEO_ENABLED,
  RILDMCONFIG_IMS_NW_ENABLED_FLAGS,
  RILDMCONFIG_IMS_IRAT_REG_DELAY,
  RILDMCONFIG_1XRTT_FALLBACK_REDIAL_TIMER,
  RILDMCONFIG_1XRTT_FALLBACK_REDIAL_ENABLE,
  RILDMCONFIG_IMS_PRESENCE_ENABLED,
  RILDMCONFIG_IMS_ROAMING_ENABLED,
  RILDMCONFIG_IMS_XCAP_ENABLED,
  RILDMCONFIG_EPDG_ADDRESS,
  RILDMCONFIG_VOWIFI_ENTITLEMENT_CHECK,
  RILDMCONFIG_RTT_MODE,
  RILDMCONFIG_MAX
} RILDMCONFIGINFOITEM;
````

## Constants

<table>

<tr>
<td>RILDMCONFIG_1XRTT_FALLBACK_REDIAL_ENABLE</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_1XRTT_FALLBACK_REDIAL_TIMER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_AMR_MODE_SET</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_AMR_SRC_CTL_RATE</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_AMR_WB_ENABLE</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_AMR_WB_MODE_SET</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_AMR_WB_SRC_CTL_RATE</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_DOMAIN_NAME</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_EPDG_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_IRAT_REG_DELAY</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_NAI</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_NW_ENABLED_FLAGS</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_PRESENCE_ENABLED</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_ROAMING_ENABLED</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_TEST_MODE_STATUS</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_VIDEO_ENABLED</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_VOICE_ENABLED</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_IMS_XCAP_ENABLED</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_MAX</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_MD5_AUTH</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_MULTIPARTY_SERVER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_PCSCF_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_PCSCF_PORT_NUMBER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_REQUEST_CONTEXT</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_RINGBACK_TIMER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_RINGING_TIMER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_RTC_INACTIVITY_TIMER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_RTT_MODE</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_SIP_SESSION_TIMER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_SIP_SESSION_TIMER_MIN</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_SIP_TIMER_F</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_SIP_TIMER_T2</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_SMS_FORMAT_TYPE</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_SMS_OVER_IP_NW_INDICATION</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_UDP_KEEPALIVE_TIMER</td>
<td></td>
</tr>

<tr>
<td>RILDMCONFIG_VOWIFI_ENTITLEMENT_CHECK</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |