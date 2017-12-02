---
UID: NC.bthsdpddi.PBYTESWAPUINT128
title: PBYTESWAPUINT128
author: windows-driver-content
description: The Bluetooth SdpByteSwapUint128 function is used to reverse the byte order of an unsigned 128-bit integer.
old-location: bltooth\sdpbyteswapuint128.htm
old-project: bltooth
ms.assetid: 04a3400a-e526-47d2-a602-6ecaa7ee7fcf
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: BTH_VENDOR_SPECIFIC_COMMAND, BTH_VENDOR_SPECIFIC_COMMAND, *PBTH_VENDOR_SPECIFIC_COMMAND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: bthsdpddi.h
req.include-header: BthSdpddi.h
req.target-type: Desktop
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SdpByteSwapUint128
req.alt-loc: sdplib.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: 
---

# PBYTESWAPUINT128 callback



## -description
<p>The Bluetooth 
  <b>SdpByteSwapUint128</b> function is used to reverse the byte order of an unsigned 128-bit integer.</p>


## -prototype

````
PBYTESWAPUINT128 SdpByteSwapUint128;

void SdpByteSwapUint128(
   PSDP_ULARGE_INTEGER_16 pInUint128,
   PSDP_ULARGE_INTEGER_16 pOutUint128
)
{ ... }
````


## -parameters
<dl>

### -param pInUint128 

<dd>
<p>A pointer to an unsigned 128-bit integer for which to reverse the byte order.</p>
</dd>

### -param pOutUint128 

<dd>
<p>A pointer to a variable that receives the converted 128-bit integer.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <b>SdpByteSwapUint128</b> function always reverses the byte order of the value passed in the 
    <i>pInUint128</i> parameter. Writers of Bluetooth device drivers can use this function to convert unsigned
    128-bit integer values from the byte order on the local computer to the byte order of the network that
    the computer is connected to.</p>

<p>Bluetooth profile drivers can obtain a pointer to this function through the 
    <a href="..\bthsdpddi\ns-bthsdpddi--bthddi-sdp-parse-interface.md">BTHDDI_SDP_PARSE_INTERFACE</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sdplib.h (include BthSdpddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\bthsdpddi\ns-bthsdpddi--bthddi-sdp-parse-interface.md">BTHDDI_SDP_PARSE_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20PBYTESWAPUINT128 callback function%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
