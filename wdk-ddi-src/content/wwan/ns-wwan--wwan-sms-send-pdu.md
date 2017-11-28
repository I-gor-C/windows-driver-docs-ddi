---
UID: NS.wwan._WWAN_SMS_SEND_PDU
title: WWAN_SMS_SEND_PDU
author: windows-driver-content
description: The WWAN_SMS_SEND_PDU structure represents a PDU-style SMS message.
old-location: netvista\wwan_sms_send_pdu.htm
old-project: netvista
ms.assetid: 94d19d5b-8fa5-437d-9359-e35ef103f380
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WWAN_SMS_SEND_PDU, WWAN_SMS_SEND_PDU, *PWWAN_SMS_SEND_PDU
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SMS_SEND_PDU
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_SMS_SEND_PDU structure



## -description
<p>The WWAN_SMS_SEND_PDU structure represents a PDU-style SMS message.</p>


## -syntax

````
typedef struct _WWAN_SMS_SEND_PDU {
  BYTE Size;
  CHAR PduData[WWAN_SMS_PDU_HEX_BUF_LEN];
} WWAN_SMS_SEND_PDU, *PWWAN_SMS_SEND_PDU;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>For GSM-based devices that support PDU-style SMS messages, the size, in bytes, of the message
     before conversion to hexadecimal.
     </p>
<p>For CDMA-based devices that support sending SMS messages in binary format, the size, in bytes, of the
     message in 
     <b>PduData</b> .</p>
<p>The following table lists the different values for the 
     <b>SmsFormat</b> member of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571250">WWAN_SMS_SEND</a> structure and their
     corresponding range that is allowed in this member.</p>
<table>
<tr>
<th>SmsFormat</th>
<th>Size</th>
</tr>
<tr>
<td>
<p>WwanSmsFormatPdu</p>
</td>
<td>
<p>1 to WWAN_SMS_RAW_PDU_LEN</p>
</td>
</tr>
<tr>
<td>
<p>WwanSmsFormatCdma</p>
</td>
<td>
<p>1 to WWAN_SMS_CDMA_MAX_MSG_LEN</p>
</td>
</tr>
</table>
<p> </p>
<div class="alert"><b>Note</b>  For GSM-based devices, if 
     <b>ElementType</b> is set to 
     <b>WwanStructSmsPdu</b>, this member describes the size, in bytes, of 
     <b>PduData</b> excluding the Service Center address. The first byte of 
     <b>PduData</b> represents the size of the Service Center address that the miniport driver must add when
     it calculates the exact size of the 
     <b>PduData</b> buffer.
     <p class="note">For example:</p>
<p class="note">If 
     <b>PduData</b> [0] = 0, then the size of 
     <b>PduData</b> is 
     <b>Size</b> + 1.</p>
<p class="note">If 
     <b>PduData</b> [0] != 0, then the size of 
     <b>PduData</b> is 
     <b>Size</b> + 
     <b>PduData</b> [0].</p>
</div>
<div> </div>
</dd>

### -field <b>PduData</b>

<dd>
<p>A NULL-terminated string that represents the content of the record.
     </p>
<p>For GSM-based devices, the contents are coded in a hexadecimal string format (according to the 3GPP
     TS 27.005 and 3GPP TS 23.040 standards) that represents the SMS text message.</p>
<p>For CDMA-based devices that support sending SMS messages in binary format (that is, miniport drivers
     that return WWAN_SMS_CAPS_PDU_SEND in the 
     <b>WwanSmsCaps</b> member of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>), 
     <b>PduData</b> contains the SMS message as a byte array, as defined in section 3.4.2.1 SMS Point-to-Point
     Message in the 3GPP2 specification C.S0015-A "Short Message Service (SMS) for Wideband Spread Spectrum
     Systems". SMS will only support Wireless Messaging Teleservice (WMT) format. Miniport drivers should
     typecast this information to BYTE[] for CDMA-based devices. It is not coded in hexadecimal string
     format.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571250">WWAN_SMS_SEND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_SEND_PDU structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
