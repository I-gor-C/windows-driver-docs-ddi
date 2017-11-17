---
UID: NS.wwan._WWAN_DEVICE_CAPS_EX
title: WWAN_DEVICE_CAPS_EX
author: windows-driver-content
description: The WWAN_DEVICE_CAPS_EX structure represents the capabilities of the mobile broadband device.
old-location: netvista\wwan_device_caps_ex.htm
ms.assetid: 91F62BFF-C26A-422A-B138-1E8D9A5146B3
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_DEVICE_CAPS_EX
req.alt-loc: wwan.h
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
ms.keywords: WWAN_DEVICE_CAPS_EX, WWAN_DEVICE_CAPS_EX, *PWWAN_DEVICE_CAPS_EX
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_DEVICE_CAPS_EX structure



## -description
<p>The <b>WWAN_DEVICE_CAPS_EX</b> structure represents the capabilities of the mobile broadband device. <b>WWAN_DEVICE_CAPS_EX</b> extends the existing <a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a> structure by adding an <b>Executor Index</b> member, for tracking specific executors, and a <b>WwanOptionalServiceCaps</b> member, for Microsoft service extensions.</p>


## -syntax

````
typedef struct _WWAN_DEVICE_CAPS_EX {
  WWAN_DEVICE_TYPE    WwanDeviceType;
  WWAN_CELLULAR_CLASS WwanCellularClass;
  WWAN_VOICE_CLASS    WwanVoiceClass;
  WWAN_SIM_CLASS      WwanSimClass;
  ULONG               WwanDataClass;
  WCHAR               CustomDataClass[WWAN_CUSTOM_DATA_CLASS_LEN];
  ULONG               WwanGsmBandClass;
  ULONG               WwanCdmaBandClass;
  WCHAR               CustomBandClass[WWAN_CUSTOM_BAND_CLASS_LEN];
  ULONG               WwanSmsCaps;
  ULONG               WwanControlCaps;
  WCHAR               DeviceId[WWAN_DEVICEID_LEN];
  WCHAR               Manufacturer[WWAN_MANUFACTURER_LEN];
  WCHAR               Model[WWAN_MODEL_LEN];
  WCHAR               FirmwareInfo[WWAN_FIRMWARE_LEN];
  ULONG               MaxActivatedContexts;
  ULONG               WwanAuthAlgoCaps;
  ULONG               ExecutorIndex;
  ULONG               WwanOptionalServiceCaps;
  WWAN_LIST_HEADER    CellularClassListHeader;
} WWAN_DEVICE_CAPS_EX, *PWWAN_DEVICE_CAPS_EX;
````


## -struct-fields
<dl>

### -field <b>WwanDeviceType</b>

<dd>
<p>The type of the device. Miniport drivers must set the device type to be a value other than 
     <b>WwanDeviceTypeUnknown</b>.</p>
</dd>

### -field <b>WwanCellularClass</b>

<dd>
<p>The cellular class of the device. Miniport drivers must set the cellular class to be a value other
     than 
     <b>WwanCellularClassUnknown</b>. The values in this member control features that are specific to
     cellular technology, such as network provider registration modes.</p>
<p>Miniport drivers that support multi-mode should set this to <b>WwanCellularClassGsm.</b></p>
</dd>

### -field <b>WwanVoiceClass</b>

<dd>
<p>The voice class of the device. This member informs the MB Service about the presence of circuit
     voice service, and how such service interacts with data service. Be aware that the MB Service does not
     support circuit-switched voice natively, nor does it preclude it. It is up to the miniport driver to
     determine how to support circuit voice. This 
     <b>WwanVoiceClass</b> member allows the MB Service to support this feature in the future.</p>
</dd>

### -field <b>WwanSimClass</b>

<dd>
<p>The class of the Subscriber Identity Module (SIM card). Miniport drivers must set the SIM class to
     be a value other than 
     <b>WwanSimClassUnknown</b>.</p>
</dd>

### -field <b>WwanDataClass</b>

<dd>
<p>A bitmap that represents the data-class(es) that the device supports. The following table shows
     the possible values for this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_NONE</p>
</td>
<td>
<p>The device does not support data service.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_GPRS</p>
</td>
<td>
<p>General Packet Radio Service (GPRS) data service is supported. This value applies only to
        GSM-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_EDGE</p>
</td>
<td>
<p>Enhanced Data for Global Evolution (EDGE) data service is supported. This value applies only to
        GSM-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_UMTS</p>
</td>
<td>
<p>Universal Mobile Telecommunications System (UMTS) data service is supported. This value applies
        only to GSM-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_HSDPA</p>
</td>
<td>
<p>High-Speed Downlink Packet Access (HSDPA) data service is supported. This value applies only to
        GSM-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_HSUPA</p>
</td>
<td>
<p>High-Speed Uplink Packet Access (HSUPA) data service is supported. This value applies only to
        GSM-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_LTE</p>
</td>
<td>
<p>LTE data service is supported. This value applies only to GSM-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_1XRTT</p>
</td>
<td>
<p>CDMA 1x Radio Transmission Technology (1xRTT, also known as cdma2000, CDMA2000 1x, and so on) data
        service is supported. This value applies only to CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_1XEVDO</p>
</td>
<td>
<p>CDMA Evolution-Data Optimized (originally Data Only, 1xEDVO, also known as CDMA2000 1x EV-DO, or
        1x EVDO) data service is supported. This value applies only to CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_1XEVDO_REVA</p>
</td>
<td>
<p>1xEVDO RevA data service is supported. This value applies only to CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_1XEVDV</p>
</td>
<td>
<p>CDMA Evolution-Data/Voice (also known as CDMA 2000 1x EV-DV, or 1x EVDV) data service is
        supported. This value applies only to CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_3XRTT</p>
</td>
<td>
<p>CDMA 3x Radio Transmission Technology (3xRTT) data service is supported. This value applies only
        to CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_1XEVDO_REVB</p>
</td>
<td>
<p>1xEVDO RevB data service is supported. This value applies only to CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_UMB</p>
</td>
<td>
<p>UMB data service is supported. This value applies only to CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_DATA_CLASS_CUSTOM</p>
</td>
<td>
<p>The device supports a data service not listed in this table.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CustomDataClass</b>

<dd>
<p>A NULL-terminated string that represents the name of the custom data-class. This member is valid
     only when the miniport driver sets the WWAN_DATA_CLASS_CUSTOM bit in the 
     <b>WwanDataClass</b> member.</p>
</dd>

### -field <b>WwanGsmBandClass</b>

<dd>
<p>A bitmap that represents the frequency bands GSM-based devices support. The following table shows
     the possible values for this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_UNKNOWN</p>
</td>
<td>
<p>The frequency band that is supported by the device is not given.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_I</p>
</td>
<td>
<p>The device supports the UMTS2100 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_II</p>
</td>
<td>
<p>The device supports the UMTS1900 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_III</p>
</td>
<td>
<p>The device supports the UMTS1800 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_IV</p>
</td>
<td>
<p>The device supports the AWS spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_V</p>
</td>
<td>
<p>The device supports the UMTS850 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_VI</p>
</td>
<td>
<p>The device supports the UMTS800 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_VII</p>
</td>
<td>
<p>The device supports the UMTS2600 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_VIII</p>
</td>
<td>
<p>The device supports the UMTS900 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_IX</p>
</td>
<td>
<p>The device supports the UMTS1700 spectrum.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_X</p>
</td>
<td></td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_CUSTOM</p>
</td>
<td>
<p>The device supports a spectrum other than those listed in this table.</p>
</td>
</tr>
</table>
<p> </p>
<p>If the miniport driver specifies WWAN_BAND_CLASS_CUSTOM, it should also provide the name of the
     data-class in 
     <b>CustomBandClass</b> .</p>
<p>For more information about these values, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569824">OID_WWAN_DEVICE_CAPS</a>.</p>
</dd>

### -field <b>WwanCdmaBandClass</b>

<dd>
<p>A bitmap that represents the frequency bands CDMA-based devices support. The following table shows
     the possible values for this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_UNKNOWN</p>
</td>
<td>
<p>The frequency band that is supported by the device is not given.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_0</p>
</td>
<td>
<p>The device supports the 800MHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_I</p>
</td>
<td>
<p>The device supports the 1900MHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_II</p>
</td>
<td>
<p>The device supports the TACS band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_III</p>
</td>
<td>
<p>The device supports the JTACS band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_IV</p>
</td>
<td>
<p>The device supports the Korean PCS band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_V</p>
</td>
<td>
<p>The device supports the 450 MHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_VI</p>
</td>
<td>
<p>The device supports the 2 GHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_VII</p>
</td>
<td>
<p>The device supports the 700 MHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_VIII</p>
</td>
<td>
<p>The device supports the 1800 MHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_IX</p>
</td>
<td>
<p>The device supports the 900 MHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_X</p>
</td>
<td>
<p>The device supports the secondary 800 MHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_XI</p>
</td>
<td>
<p>The device supports the 400 MHz European PAMR band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_XII</p>
</td>
<td>
<p>The device supports the 800 MHz PAMR band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_XIII</p>
</td>
<td>
<p>The device supports the 2.5GHz IMT2000 Extension band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_XIV</p>
</td>
<td>
<p>The device supports the US PCS 1.9GHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_XV</p>
</td>
<td>
<p>The device supports the AWS band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_XVI</p>
</td>
<td>
<p>The device supports the US 2.5GHz band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_XVII</p>
</td>
<td>
<p>The device supports the US 2.5 GHz Forward Link Only band.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_BAND_CLASS_CUSTOM</p>
</td>
<td>
<p>The device supports a band other than the bands listed in this table.</p>
</td>
</tr>
</table>
<p> </p>
<p>If the miniport driver specifies WWAN_BAND_CLASS_CUSTOM, it should also provide the name of the
     data-class in 
     <b>CustomBandClass</b> .</p>
<p>For more information about these values, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569824">OID_WWAN_DEVICE_CAPS</a>.</p>
</dd>

### -field <b>CustomBandClass</b>

<dd>
<p>A NULL-terminated string that represents the name of the custom band class. This member is valid
     only when the miniport driver sets the WWAN_BAND_CLASS_CUSTOM bit in either the 
     <b>WwanGsmBandClass</b> or 
     <b>WwanCdmaBandClass</b> members, as appropriate.</p>
</dd>

### -field <b>WwanSmsCaps</b>

<dd>
<p>A bitmap that represents the type of SMS messages and directional flow that the device supports.
     The following table shows the valid SMS capabilities settings.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_SMS_CAPS_NONE</p>
</td>
<td>
<p>The device does not support SMS messages.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_SMS_CAPS_PDU_SEND</p>
</td>
<td>
<p>For GSM-based devices, this value means that the device supports sending PDU-style SMS
        messages.</p>
<p>For CDMA-based devices, this value means that the device is capable of sending SMS messages in
        binary format as defined in section "3.4.2.1 SMS Point-to-Point Message" in 3GPP2 specification
        C.S0015-A "Short Message Service (SMS) for Wideband Spread Spectrum Systems".</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_SMS_CAPS_PDU_RECEIVE</p>
</td>
<td>
<p>For GSM-based devices, this value means that the device supports receiving PDU-style SMS
        messages.</p>
<p>For CDMA-based devices, this value means that the device is capable of reading the SMS messages in
        binary format as defined in section "3.4.2.1 SMS Point-to-Point Message" in the 3GPP2 specification
        C.S0015-A "Short Message Service (SMS) for Wideband Spread Spectrum Systems".</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_SMS_CAPS_TEXT_SEND</p>
</td>
<td>
<p>The device supports sending Text-style SMS messages. This flag applies for CDMA-based devices.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_SMS_CAPS_TEXT_RECEIVE</p>
</td>
<td>
<p>The device supports receiving Text-style SMS messages. This flag applies for CDMA-based
        devices.</p>
</td>
</tr>
</table>
<p> </p>
<p>Miniport drivers should set this member to reflect support for only GSM PDU format for receiving and sending SMS when the current home provider is multi-mode capable. Therefure, if the miniport driver receives a SMS in the cellular class native format, for example CDMA TEXT or CDMA PDU, then the miniport driver is required to do the translation to GSM PDU and indicate it to the MB Service. Similarly if the miniport driver receives a send request in GSM PDU format then it is required to do the translation to its native cellular class format.</p>
</dd>

### -field <b>WwanControlCaps</b>

<dd>
<p>A bitmap that represents the control capabilities that the device supports. The following table
     shows the valid WwanControlCaps settings for GSM-based and CDMA-based devices. 
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_REG_MANUAL</p>
</td>
<td>
<p>Indicates whether the provider network allows manual network selection. Miniport drivers for
        GSM-based devices should specify this flag. Miniport drivers for CDMA-based devices should not
        specify this flag.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_HW_RADIO_SWITCH</p>
</td>
<td>
<p>Indicates the presence of a hardware radio power switch. This corresponds to the 
        <b>WwanDeviceTypeEmbedded</b> value of the WWAN_DEVICE_TYPE enumeration.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_CDMA_MOBILE_IP</p>
</td>
<td>
<p>Indicates that the CDMA-based device is configured to support mobile IP. This flag applies only to
        CDMA-based devices.</p>
<p>Miniport drivers should not set this flag when the current home provider is multi-mode capable.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_CDMA_SIMPLE_IP</p>
</td>
<td>
<p>Indicates that the CDMA-based device is configured for simple IP support. This flag applies only
        to CDMA-based devices.</p>
<p>Miniport drivers should not set this flag when the current home provider is multi-mode capable.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_CDMA_MOBILE_IP ored with WWAN_CTRL_CAPS_CDMA_SIMPLE_IP</p>
</td>
<td>
<p>Indicates that the CDMA-based device is configured to support mobile IP, with simple IP as a
        fallback option.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_PROTECT_UNIQUEID</p>
</td>
<td>
<p>Indicates that Windows should not display the International Mobile Subscriber Identity (IMSI).</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_USSD</p>
</td>
<td>
<p>Indicates that the GSM-based MB device is configured to support the USSD protocol. This flag applies only to GSM-based devices.</p>
<p>Miniport drivers that support sending and receiving USSD messages set this flag.</p>
<p>Miniport drivers can set this flag  when the current multi-mode capable home providers GSM side of the network supports USSD even if the CDMA side of the network does not support USSD.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_MODEL_MULTI_CARRIER</p>
</td>
<td>
<p>Indicates that the MB device supports registering and connecting to multiple network operators.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_CTRL_CAPS_MULTI_MODE</p>
</td>
<td>
<p>This flag indicates that the current home provider supports multiple cellular classes/RATs (Radio Access Technologies).</p>
</td>
</tr>
</table>
<p> </p>
<p>Miniport drivers of CDMA-based devices must specify WWAN_CTRL_CAPS_CDMA_MOBILE_IP, or
     WWAN_CTRL_CAPS_CDMA_SIMPLE_IP, or both flags to inform the MB Service about the type of IP that the
     device supports.</p>
</dd>

### -field <b>DeviceId</b>

<dd>
<p>A NULL-terminated string that represents the device ID.</p>
<p>For GSM-based devices, the string must
     conform to the International Mobile Equipment Identity (IMEI) format (up to 15 digits).</p>
<p>For CDMA-based
     devices, the string must conform to both the Electronic Serial Number (ESN, 11 digits) and Mobile
     Equipment Identifier (MEID, 17 digits) formats.</p>
<p>For multi-mode capable miniport drivers, for example those that set the <b>WWAN_CTRL_CAPS_MULTI_MODE</b> flag in <b>WwanControlCaps</b>, only the GSM-based <b>DeviceId</b> must be reported.</p>
<p>This value should be stored in the device's memory and
     must be available even when the MB device/SIM requires a PIN to unlock.</p>
</dd>

### -field <b>Manufacturer</b>

<dd>
<p>A NULL-terminated string that represents the manufacturer of the device. This member is
     optional.</p>
</dd>

### -field <b>Model</b>

<dd>
<p>A NULL-terminated string that represents the model of the device. This member is optional.</p>
</dd>

### -field <b>FirmwareInfo</b>

<dd>
<p>A NULL-terminated string that represents the firmware specific information about the device. This
     member is optional.</p>
</dd>

### -field <b>MaxActivatedContexts</b>

<dd>
<p>The maximum number of activated contexts that are supported by the device. Miniport drivers should
     enforce this limit by failing any activation attempts that exceed 
     <b>MaxActivatedContexts</b>.</p>
</dd>

### -field <b>WwanAuthAlgoCaps</b>

<dd>
<p>A bitmap that represents the types of authentication methods the MB device supports.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_AUTH_ALGO_CAPS_NONE</p>
</td>
<td>
<p>The MB device does not support any authentication methods.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_AUTH_ALGO_CAPS_SIM</p>
</td>
<td>
<p>The MB device supports the SIM authentication method.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_AUTH_ALGO_CAPS_AKA</p>
</td>
<td>
<p>The MB device supports the AKA authentication method.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_AUTH_ALGO_CAPS_AKAP</p>
</td>
<td>
<p>The MB device supports the AKA' (AKA Prime) authentication method.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ExecutorIndex</b>

<dd>
<p>The <b>WwanDeviceType</b> member for <b>WWAN_DEVICE_CAPS_EX</b> no longer refers to the modem device but rather to an individual executor. Each device is an RF executor entity of which the OS is aware.</p>
</dd>

### -field <b>WwanOptionalServiceCaps</b>

<dd>
<p>A ULONG structure that represents the Microsoft service extensions the underlying modem supports. It is a 64-bit bitmap structure that whose undefined bits are reserved and must be set to "0." As new service extensions are introduced, the reserved bits will be used to represent the new service extensions.</p>
<table>
<tr>
<th>Value</th>
<th>Mask</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_OPTIONAL_SERVICE_CAPS_NONE</p>
</td>
<td>
<p>0h</p>
</td>
<td>
<p>The device and driver do not support optional service extensions.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_OPTIONAL_SERVICE_CAPS_LTE_ATTACH</p>
</td>
<td>
<p>1h</p>
</td>
<td>
<p> The device and driver support LTE attach configuration and the following MBIM CIDs:</p>
<ul>
<li>MBIM_CID_MS_LTE_ATTACH_CONFIG</li>
<li>MBIM_CID_MS_LTE_ATTACH_STATUS</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>WWAN_OPTIONAL_SERVICE_CAPS_CONTEXT_MGMT</p>
</td>
<td>
<p>2h</p>
</td>
<td>
<p>The device and driver support the OS managing modem provisioned contexts and the following MBIM CID:</p>
<ul>
<li>MBIM_CID_PROVISIONED_CONTEXT_V2</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>WWAN_OPTIONAL_SERVICE_CAPS_MULTI_SIM</p>
</td>
<td>
<p>4h</p>
</td>
<td>
<p>The device and driver support multi-SIM/multi-executors and the following OIDs:</p>
<ul>
<li>
<a href="netvista.oid_wwan_sys_caps">OID_WWAN_SYS_CAPS_INFO</a>
</li>
<li>
<a href="netvista.oid_wwan_device_slot_mappings">OID_WWAN_DEVICE_SLOT_MAPPING_INFO</a>
</li>
<li>
<a href="netvista.oid_wwan_slot_info_status">OID_WWAN_SLOT_INFO</a>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>WWAN_OPTIONAL_SERVICE_CAPS_EX_SAR</p>
</td>
<td>
<p>8h</p>
</td>
<td>
<p>The device and driver support SAR configuration from the OS and the following MBIM CIDs:</p>
<ul>
<li>MBIM_CID_MS_SAR_CONFIG</li>
<li>MBIM_CID_MS_TRANSMISSION_STATUS</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>WWAN_OPTIONAL_SERVICE_CAPS_NETWORK_BLACKLIST</p>
</td>
<td>
<p>16h</p>
</td>
<td>
<p>The device and driver support network blacklist configuration from the OS and the following MBIM CID:</p>
<ul>
<li>MBIM_CID_MS_NETWORK_BLACKLIST</li>
</ul>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CellularClassListHeader</b>

<dd>
<p>A formatted WWAN_LIST_HEADER object that represents a list of cellular classes that a multi-mode capable device supports. The <b>ElementType</b> member in WWAN_LIST_HEADER should always be set to <b>WwanStructCellularClass</b>. The <b>ElementCount</b> member in WWAN_LIST_HEADER is set to the number of cellular classes that follow the WWAN_LIST_HEADER structure. MB devices that are not multi-mode capable should set <b>ElementCount</b> to 0.</p>
</dd>
</dl>

## -remarks
<p>Miniport drivers should specify WWAN_DATA_CLASS_CUSTOM if the data service supported by the device
    does not belong to any of the other values defined in the table for the 
    <b>WwanDataClass</b> member. If a miniport driver sets the WWAN_DATA_CLASS_CUSTOM flag, the miniport
    driver should also provide the name of the data-class in the 
    <b>CustomDataClass</b> member.</p>

<p>For GSM-based devices, only GSM-based data-classes must be specified. For example, GPRS, EDGE, UMTS,
    HSDPA, LTE, and TD-SCDMA. If your miniport driver supports TD-SCDMA, then it should specify
    WWAN_DATA_CLASS_CUSTOM in the 
    <b>WwanDataClass</b> member and the string "TD-SCDMA" in the 
    <b>CustomDataClass</b> member.</p>

<p>For CDMA-based devices, only CDMA-related data services must be specified. For example, 1xRTT,
    1xEV-DO, 1xEV-DO RevA, and UMB. 1xEV-DO RevB is defined for future use. 1xEV-DV and 3xRTT are also
    defined for completeness.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/FC801FA3-699F-4EE5-BED9-35CA696A5E52">NDIS_WWAN_DEVICE_CAPS_EX</a>
</dt>
<dt>
<a href="netvista.oid_wwan_device_caps_ex">OID_WWAN_DEVICE_CAPS_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DEVICE_CAPS_EX structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
