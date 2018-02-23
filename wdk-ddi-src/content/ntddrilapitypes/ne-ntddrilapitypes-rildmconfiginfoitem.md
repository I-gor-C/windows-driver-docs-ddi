---
UID: NE:ntddrilapitypes.RILDMCONFIGINFOITEM
title: RILDMCONFIGINFOITEM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildmconfiginfoitem.htm
old-project: netvista
ms.assetid: 31061811-e148-4af2-8a9b-370d1b45ae1f
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: netvista.rildmconfiginfoitem, ntddrilapitypes/RILDMCONFIG_MULTIPARTY_SERVER, RILDMCONFIG_IMS_NW_ENABLED_FLAGS, ntddrilapitypes/RILDMCONFIG_IMS_XCAP_ENABLED, RILDMCONFIG_MD5_AUTH, RILDMCONFIG_PCSCF_PORT_NUMBER, RILDMCONFIG_RINGING_TIMER, RILDMCONFIG_SIP_TIMER_T2, ntddrilapitypes/RILDMCONFIG_DOMAIN_NAME, ntddrilapitypes/RILDMCONFIG_IMS_NAI, ntddrilapitypes/RILDMCONFIG_RINGING_TIMER, ntddrilapitypes/RILDMCONFIG_RTC_INACTIVITY_TIMER, RILDMCONFIG_AMR_WB_ENABLE, ntddrilapitypes/RILDMCONFIG_SIP_SESSION_TIMER, RILDMCONFIG_REQUEST_CONTEXT, RILDMCONFIG_SIP_SESSION_TIMER, RILDMCONFIGINFOITEM, ntddrilapitypes/RILDMCONFIG_MD5_AUTH, RILDMCONFIG_AMR_WB_MODE_SET, RILDMCONFIG_1XRTT_FALLBACK_REDIAL_ENABLE, RILDMCONFIG_IMS_PRESENCE_ENABLED, ntddrilapitypes/RILDMCONFIG_VOWIFI_ENTITLEMENT_CHECK, RILDMCONFIG_IMS_TEST_MODE_STATUS, RILDMCONFIG_MULTIPARTY_SERVER, RILDMCONFIG_IMS_VOICE_ENABLED, ntddrilapitypes/RILDMCONFIG_1XRTT_FALLBACK_REDIAL_TIMER, RILDMCONFIG_SMS_FORMAT_TYPE, ntddrilapitypes/RILDMCONFIG_1XRTT_FALLBACK_REDIAL_ENABLE, RILDMCONFIG_IMS_IRAT_REG_DELAY, RILDMCONFIG_AMR_WB_SRC_CTL_RATE, ntddrilapitypes/RILDMCONFIG_SIP_TIMER_F, ntddrilapitypes/RILDMCONFIG_RINGBACK_TIMER, RILDMCONFIG_UDP_KEEPALIVE_TIMER, ntddrilapitypes/RILDMCONFIG_UDP_KEEPALIVE_TIMER, ntddrilapitypes/RILDMCONFIG_IMS_IRAT_REG_DELAY, ntddrilapitypes/RILDMCONFIG_AMR_SRC_CTL_RATE, ntddrilapitypes/RILDMCONFIG_SMS_FORMAT_TYPE, ntddrilapitypes/RILDMCONFIG_SIP_TIMER_T2, ntddrilapitypes/RILDMCONFIG_IMS_TEST_MODE_STATUS, RILDMCONFIG_PCSCF_ADDRESS, RILDMCONFIGINFOITEM enumeration [Network Drivers Starting with Windows Vista], RILDMCONFIG_SIP_SESSION_TIMER_MIN, RILDMCONFIG_IMS_NAI, ntddrilapitypes/RILDMCONFIG_AMR_WB_MODE_SET, ntddrilapitypes/RILDMCONFIG_IMS_VOICE_ENABLED, ntddrilapitypes/RILDMCONFIG_IMS_NW_ENABLED_FLAGS, ntddrilapitypes/RILDMCONFIG_AMR_WB_ENABLE, ntddrilapitypes/RILDMCONFIG_RTT_MODE, ntddrilapitypes/RILDMCONFIG_EPDG_ADDRESS, ntddrilapitypes/RILDMCONFIGINFOITEM, ntddrilapitypes/RILDMCONFIG_IMS_VIDEO_ENABLED, RILDMCONFIG_AMR_MODE_SET, RILDMCONFIG_IMS_XCAP_ENABLED, ntddrilapitypes/RILDMCONFIG_PCSCF_PORT_NUMBER, RILDMCONFIG_SIP_TIMER_F, RILDMCONFIG_MAX, RILDMCONFIG_EPDG_ADDRESS, ntddrilapitypes/RILDMCONFIG_SMS_OVER_IP_NW_INDICATION, ntddrilapitypes/RILDMCONFIG_AMR_WB_SRC_CTL_RATE, ntddrilapitypes/RILDMCONFIG_IMS_PRESENCE_ENABLED, RILDMCONFIG_SMS_OVER_IP_NW_INDICATION, RILDMCONFIG_AMR_SRC_CTL_RATE, ntddrilapitypes/RILDMCONFIG_AMR_MODE_SET, RILDMCONFIG_VOWIFI_ENTITLEMENT_CHECK, ntddrilapitypes/RILDMCONFIG_MAX, RILDMCONFIG_IMS_ROAMING_ENABLED, RILDMCONFIG_RTT_MODE, RILDMCONFIG_DOMAIN_NAME, RILDMCONFIG_1XRTT_FALLBACK_REDIAL_TIMER, ntddrilapitypes/RILDMCONFIG_SIP_SESSION_TIMER_MIN, RILDMCONFIG_RTC_INACTIVITY_TIMER, RILDMCONFIG_IMS_VIDEO_ENABLED, ntddrilapitypes/RILDMCONFIG_IMS_ROAMING_ENABLED, ntddrilapitypes/RILDMCONFIG_PCSCF_ADDRESS, ntddrilapitypes/RILDMCONFIG_REQUEST_CONTEXT, RILDMCONFIG_RINGBACK_TIMER
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
-	ntddrilapitypes.h
apiname:
-	RILDMCONFIGINFOITEM
product: Windows
targetos: Windows
req.typenames: RILDMCONFIGINFOITEM
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
                    <td>RILDMCONFIG_SIP_TIMER_T1</td>
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
| **Header** | ntddrilapitypes.h |