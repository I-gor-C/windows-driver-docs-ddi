---
UID: NS.hbapiwmi._SendRNIDV2_OUT
title: SendRNIDV2_OUT
author: windows-driver-content
description: The SendRNIDV2_OUT structure is used to report the output parameter data of the SendRNIDV2 WMI method to the WMI client.
old-location: storage\sendrnidv2_out.htm
old-project: storage
ms.assetid: 2d8f1b49-5add-4dd9-998f-d0c1e79f3e7d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SendRNIDV2_OUT, SendRNIDV2_OUT, *PSendRNIDV2_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SendRNIDV2_OUT
req.alt-loc: hbapiwmi.h
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

# SendRNIDV2_OUT structure



## -description
<p>The SendRNIDV2_OUT structure is used to report the output parameter data of the <a href="storage.sendrnidv2">SendRNIDV2</a> WMI method to the WMI client.</p>


## -syntax

````
typedef struct _SendRNIDV2_OUT {
  ULONG HBAStatus;
  ULONG TotalRspBufferSize;
  ULONG ActualRspBufferSize;
  UCHAR RspBuffer[1];
} SendRNIDV2_OUT, *PSendRNIDV2_OUT;
````


## -struct-fields
<dl>

### -field HBAStatus

<dd>
<p>Contains the status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>. </p>
</dd>

### -field TotalRspBufferSize

<dd>
<p>Contains the size in bytes of the results of the version 2 request node identification data (RNIDV2) command. </p>
</dd>

### -field ActualRspBufferSize

<dd>
<p>Contains the size in bytes of the data that was actually retrieved. </p>
</dd>

### -field RspBuffer

<dd>
<p>Contains the results of the RNIDV2 command. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SendRNIDV2_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbaadaptermethods_wmi_class">MSFC_HBAAdapterMethods WMI Class</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.sendrnidv2">SendRNIDV2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SendRNIDV2_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
