---
UID: NE.ntddrilapitypes.RILDMCONFIGINFOITEM
title: RILDMCONFIGINFOITEM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildmconfiginfoitem.htm
old-project: netvista
ms.assetid: 31061811-e148-4af2-8a9b-370d1b45ae1f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILDMCONFIGINFOITEM
req.alt-loc: ntddrilapitypes.h
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
req.iface: 
---

# RILDMCONFIGINFOITEM enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

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


## -enum-fields
<dl>

### -field RILDMCONFIG_SIP_TIMER_T2

<dd></dd>

### -field RILDMCONFIG_SIP_TIMER_F

<dd></dd>

### -field RILDMCONFIG_SMS_FORMAT_TYPE

<dd></dd>

### -field RILDMCONFIG_DOMAIN_NAME

<dd></dd>

### -field RILDMCONFIG_SMS_OVER_IP_NW_INDICATION

<dd></dd>

### -field RILDMCONFIG_IMS_TEST_MODE_STATUS

<dd></dd>

### -field RILDMCONFIG_PCSCF_ADDRESS

<dd></dd>

### -field RILDMCONFIG_PCSCF_PORT_NUMBER

<dd></dd>

### -field RILDMCONFIG_MD5_AUTH

<dd></dd>

### -field RILDMCONFIG_MULTIPARTY_SERVER

<dd></dd>

### -field RILDMCONFIG_REQUEST_CONTEXT

<dd></dd>

### -field RILDMCONFIG_IMS_NAI

<dd></dd>

### -field RILDMCONFIG_SIP_SESSION_TIMER

<dd></dd>

### -field RILDMCONFIG_SIP_SESSION_TIMER_MIN

<dd></dd>

### -field RILDMCONFIG_AMR_WB_ENABLE

<dd></dd>

### -field RILDMCONFIG_AMR_SRC_CTL_RATE

<dd></dd>

### -field RILDMCONFIG_AMR_WB_SRC_CTL_RATE

<dd></dd>

### -field RILDMCONFIG_AMR_MODE_SET

<dd></dd>

### -field RILDMCONFIG_AMR_WB_MODE_SET

<dd></dd>

### -field RILDMCONFIG_RINGING_TIMER

<dd></dd>

### -field RILDMCONFIG_RINGBACK_TIMER

<dd></dd>

### -field RILDMCONFIG_RTC_INACTIVITY_TIMER

<dd></dd>

### -field RILDMCONFIG_UDP_KEEPALIVE_TIMER

<dd></dd>

### -field RILDMCONFIG_IMS_VOICE_ENABLED

<dd></dd>

### -field RILDMCONFIG_IMS_VIDEO_ENABLED

<dd></dd>

### -field RILDMCONFIG_IMS_NW_ENABLED_FLAGS

<dd></dd>

### -field RILDMCONFIG_IMS_IRAT_REG_DELAY

<dd></dd>

### -field RILDMCONFIG_1XRTT_FALLBACK_REDIAL_TIMER

<dd></dd>

### -field RILDMCONFIG_1XRTT_FALLBACK_REDIAL_ENABLE

<dd></dd>

### -field RILDMCONFIG_IMS_PRESENCE_ENABLED

<dd></dd>

### -field RILDMCONFIG_IMS_ROAMING_ENABLED

<dd></dd>

### -field RILDMCONFIG_IMS_XCAP_ENABLED

<dd></dd>

### -field RILDMCONFIG_EPDG_ADDRESS

<dd></dd>

### -field RILDMCONFIG_VOWIFI_ENTITLEMENT_CHECK

<dd></dd>

### -field RILDMCONFIG_RTT_MODE

<dd></dd>

### -field RILDMCONFIG_MAX

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>