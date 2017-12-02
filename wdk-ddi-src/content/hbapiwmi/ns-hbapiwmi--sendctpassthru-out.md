---
UID: NS.hbapiwmi._SendCTPassThru_OUT
title: SendCTPassThru_OUT
author: windows-driver-content
description: The SendCTPassThru_OUT structure is used to report the output parameter data of the SendCTPassThru WMI method to the WMI client.
old-location: storage\sendctpassthru_out.htm
old-project: storage
ms.assetid: f9340f0d-4f70-4751-b339-de11ee13a469
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SendCTPassThru_OUT, SendCTPassThru_OUT, *PSendCTPassThru_OUT
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
req.alt-api: SendCTPassThru_OUT
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

# SendCTPassThru_OUT structure



## -description
<p>The SendCTPassThru_OUT structure is used to report the output parameter data of the <a href="storage.sendctpassthru">SendCTPassThru</a> WMI method to the WMI client.</p>


## -syntax

````
typedef struct _SendCTPassThru_OUT {
  ULONG HBAStatus;
  ULONG TotalResponseBufferCount;
  ULONG ActualResponseBufferCount;
  UCHAR ResponseBuffer[1];
} SendCTPassThru_OUT, *PSendCTPassThru_OUT;
````


## -struct-fields
<dl>

### -field HBAStatus

<dd>
<p>Contains the status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>. </p>
</dd>

### -field TotalResponseBufferCount

<dd>
<p>Contains the size in bytes of the results common transport (CT) command. </p>
</dd>

### -field ActualResponseBufferCount

<dd>
<p>Contains the size in bytes of the data that was actually retrieved. </p>
</dd>

### -field ResponseBuffer

<dd>
<p>Contains the results of the common transport command. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SendCTPassThru_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbaadaptermethods_wmi_class">MSFC_HBAAdapterMethods WMI Class</a>.</p>

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
<a href="storage.sendctpassthru">SendCTPassThru</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SendCTPassThru_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
