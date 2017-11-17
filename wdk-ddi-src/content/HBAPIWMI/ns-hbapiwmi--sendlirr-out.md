---
UID: NS.hbapiwmi._SendLIRR_OUT
title: SendLIRR_OUT
author: windows-driver-content
description: The SendLIRR_OUT structure is used to report the output parameter data of the SendLIRR WMI method to the WMI client.
old-location: storage\sendlirr_out.htm
ms.assetid: 842842c2-ed79-4c8a-b9c1-d73c47998f91
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SendLIRR_OUT
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
ms.keywords: SendLIRR_OUT, SendLIRR_OUT, *PSendLIRR_OUT
req.iface: 
---

# SendLIRR_OUT structure



## -description
<p>The SendLIRR_OUT structure is used to report the output parameter data of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565419">SendLIRR</a> WMI method to the WMI client.</p>


## -syntax

````
typedef struct _SendLIRR_OUT {
  ULONG HBAStatus;
  ULONG TotalRspBufferSize;
  ULONG ActualRspBufferSize;
  UCHAR RspBuffer[1];
} SendLIRR_OUT, *PSendLIRR_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>Contains the status of the operation. For a list of allowed values and their descriptions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>. </p>
</dd>

### -field <b>TotalRspBufferSize</b>

<dd>
<p>Contains the size in bytes of the results of the LIRR command. </p>
</dd>

### -field <b>ActualRspBufferSize</b>

<dd>
<p>Contains the size in bytes of the data that was actually retrieved. </p>
</dd>

### -field <b>RspBuffer</b>

<dd>
<p>Contains the results of the LIRR command. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SendLIRR_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562506">MSFC_HBAAdapterMethods WMI Class</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565419">SendLIRR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20SendLIRR_OUT structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
