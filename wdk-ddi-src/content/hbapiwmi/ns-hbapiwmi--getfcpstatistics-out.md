---
UID: NS.hbapiwmi._GetFCPStatistics_OUT
title: GetFCPStatistics_OUT
author: windows-driver-content
description: The GetFCPStatistics_OUT structure is used by the miniport driver to report the output parameters of the GetFCPStatistics WMI method.
old-location: storage\getfcpstatistics_out.htm
old-project: storage
ms.assetid: 150773a3-a3a9-41a7-9985-4387bba5a766
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetFCPStatistics_OUT, GetFCPStatistics_OUT, *PGetFCPStatistics_OUT
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
req.alt-api: GetFCPStatistics_OUT
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

# GetFCPStatistics_OUT structure



## -description
<p>The GetFCPStatistics_OUT structure is used by the miniport driver to report the output parameters of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554939">GetFCPStatistics</a> WMI method. </p>


## -syntax

````
typedef struct _GetFCPStatistics_OUT {
  ULONG              HBAStatus;
  MSFC_FC4STATISTICS FC4Statistics;
} GetFCPStatistics_OUT, *PGetFCPStatistics_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>Contains a value associated with the WMI class qualifier <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the result of an HBA query operation.</p>
</dd>

### -field <b>FC4Statistics</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff562492">MSFC_FC4STATISTICS</a> that holds statistics for the specified FC-4 protocol.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the GetFCPStatistics_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562506">MSFC_HBAAdapterMethods WMI Class</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554939">GetFCPStatistics</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554942">GetFCPStatistics_IN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GetFCPStatistics_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
