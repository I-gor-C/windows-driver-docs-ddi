---
UID: NE.ntddrilapitypes.RILDMCONFIGINFOITEM
title: RILDMCONFIGINFOITEM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildmconfiginfoitem.htm
ms.assetid: 31061811-e148-4af2-8a9b-370d1b45ae1f
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
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

### -field <a id="RILDMCONFIG_SIP_TIMER_T2"></a><a id="rildmconfig_sip_timer_t2"></a><b>RILDMCONFIG_SIP_TIMER_T2</b>

<dd></dd>

### -field <a id="RILDMCONFIG_SIP_TIMER_F"></a><a id="rildmconfig_sip_timer_f"></a><b>RILDMCONFIG_SIP_TIMER_F</b>

<dd></dd>

### -field <a id="RILDMCONFIG_SMS_FORMAT_TYPE"></a><a id="rildmconfig_sms_format_type"></a><b>RILDMCONFIG_SMS_FORMAT_TYPE</b>

<dd></dd>

### -field <a id="RILDMCONFIG_DOMAIN_NAME"></a><a id="rildmconfig_domain_name"></a><b>RILDMCONFIG_DOMAIN_NAME</b>

<dd></dd>

### -field <a id="RILDMCONFIG_SMS_OVER_IP_NW_INDICATION"></a><a id="rildmconfig_sms_over_ip_nw_indication"></a><b>RILDMCONFIG_SMS_OVER_IP_NW_INDICATION</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_TEST_MODE_STATUS"></a><a id="rildmconfig_ims_test_mode_status"></a><b>RILDMCONFIG_IMS_TEST_MODE_STATUS</b>

<dd></dd>

### -field <a id="RILDMCONFIG_PCSCF_ADDRESS"></a><a id="rildmconfig_pcscf_address"></a><b>RILDMCONFIG_PCSCF_ADDRESS</b>

<dd></dd>

### -field <a id="RILDMCONFIG_PCSCF_PORT_NUMBER"></a><a id="rildmconfig_pcscf_port_number"></a><b>RILDMCONFIG_PCSCF_PORT_NUMBER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_MD5_AUTH"></a><a id="rildmconfig_md5_auth"></a><b>RILDMCONFIG_MD5_AUTH</b>

<dd></dd>

### -field <a id="RILDMCONFIG_MULTIPARTY_SERVER"></a><a id="rildmconfig_multiparty_server"></a><b>RILDMCONFIG_MULTIPARTY_SERVER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_REQUEST_CONTEXT"></a><a id="rildmconfig_request_context"></a><b>RILDMCONFIG_REQUEST_CONTEXT</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_NAI"></a><a id="rildmconfig_ims_nai"></a><b>RILDMCONFIG_IMS_NAI</b>

<dd></dd>

### -field <a id="RILDMCONFIG_SIP_SESSION_TIMER"></a><a id="rildmconfig_sip_session_timer"></a><b>RILDMCONFIG_SIP_SESSION_TIMER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_SIP_SESSION_TIMER_MIN"></a><a id="rildmconfig_sip_session_timer_min"></a><b>RILDMCONFIG_SIP_SESSION_TIMER_MIN</b>

<dd></dd>

### -field <a id="RILDMCONFIG_AMR_WB_ENABLE"></a><a id="rildmconfig_amr_wb_enable"></a><b>RILDMCONFIG_AMR_WB_ENABLE</b>

<dd></dd>

### -field <a id="RILDMCONFIG_AMR_SRC_CTL_RATE"></a><a id="rildmconfig_amr_src_ctl_rate"></a><b>RILDMCONFIG_AMR_SRC_CTL_RATE</b>

<dd></dd>

### -field <a id="RILDMCONFIG_AMR_WB_SRC_CTL_RATE"></a><a id="rildmconfig_amr_wb_src_ctl_rate"></a><b>RILDMCONFIG_AMR_WB_SRC_CTL_RATE</b>

<dd></dd>

### -field <a id="RILDMCONFIG_AMR_MODE_SET"></a><a id="rildmconfig_amr_mode_set"></a><b>RILDMCONFIG_AMR_MODE_SET</b>

<dd></dd>

### -field <a id="RILDMCONFIG_AMR_WB_MODE_SET"></a><a id="rildmconfig_amr_wb_mode_set"></a><b>RILDMCONFIG_AMR_WB_MODE_SET</b>

<dd></dd>

### -field <a id="RILDMCONFIG_RINGING_TIMER"></a><a id="rildmconfig_ringing_timer"></a><b>RILDMCONFIG_RINGING_TIMER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_RINGBACK_TIMER"></a><a id="rildmconfig_ringback_timer"></a><b>RILDMCONFIG_RINGBACK_TIMER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_RTC_INACTIVITY_TIMER"></a><a id="rildmconfig_rtc_inactivity_timer"></a><b>RILDMCONFIG_RTC_INACTIVITY_TIMER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_UDP_KEEPALIVE_TIMER"></a><a id="rildmconfig_udp_keepalive_timer"></a><b>RILDMCONFIG_UDP_KEEPALIVE_TIMER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_VOICE_ENABLED"></a><a id="rildmconfig_ims_voice_enabled"></a><b>RILDMCONFIG_IMS_VOICE_ENABLED</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_VIDEO_ENABLED"></a><a id="rildmconfig_ims_video_enabled"></a><b>RILDMCONFIG_IMS_VIDEO_ENABLED</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_NW_ENABLED_FLAGS"></a><a id="rildmconfig_ims_nw_enabled_flags"></a><b>RILDMCONFIG_IMS_NW_ENABLED_FLAGS</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_IRAT_REG_DELAY"></a><a id="rildmconfig_ims_irat_reg_delay"></a><b>RILDMCONFIG_IMS_IRAT_REG_DELAY</b>

<dd></dd>

### -field <a id="RILDMCONFIG_1XRTT_FALLBACK_REDIAL_TIMER"></a><a id="rildmconfig_1xrtt_fallback_redial_timer"></a><b>RILDMCONFIG_1XRTT_FALLBACK_REDIAL_TIMER</b>

<dd></dd>

### -field <a id="RILDMCONFIG_1XRTT_FALLBACK_REDIAL_ENABLE"></a><a id="rildmconfig_1xrtt_fallback_redial_enable"></a><b>RILDMCONFIG_1XRTT_FALLBACK_REDIAL_ENABLE</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_PRESENCE_ENABLED"></a><a id="rildmconfig_ims_presence_enabled"></a><b>RILDMCONFIG_IMS_PRESENCE_ENABLED</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_ROAMING_ENABLED"></a><a id="rildmconfig_ims_roaming_enabled"></a><b>RILDMCONFIG_IMS_ROAMING_ENABLED</b>

<dd></dd>

### -field <a id="RILDMCONFIG_IMS_XCAP_ENABLED"></a><a id="rildmconfig_ims_xcap_enabled"></a><b>RILDMCONFIG_IMS_XCAP_ENABLED</b>

<dd></dd>

### -field <a id="RILDMCONFIG_EPDG_ADDRESS"></a><a id="rildmconfig_epdg_address"></a><b>RILDMCONFIG_EPDG_ADDRESS</b>

<dd></dd>

### -field <a id="RILDMCONFIG_VOWIFI_ENTITLEMENT_CHECK"></a><a id="rildmconfig_vowifi_entitlement_check"></a><b>RILDMCONFIG_VOWIFI_ENTITLEMENT_CHECK</b>

<dd></dd>

### -field <a id="RILDMCONFIG_RTT_MODE"></a><a id="rildmconfig_rtt_mode"></a><b>RILDMCONFIG_RTT_MODE</b>

<dd></dd>

### -field <a id="RILDMCONFIG_MAX"></a><a id="rildmconfig_max"></a><b>RILDMCONFIG_MAX</b>

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