---
UID: NF.ks.KsPinDataIntersectionEx
title: KsPinDataIntersectionEx
author: windows-driver-content
description: The KsPinDataIntersectionEx function handles the KSPROPERTY_PIN_DATAINTERSECTION through a callback function.
old-location: stream\kspindataintersectionex.htm
old-project: stream
ms.assetid: 4d471d91-7b2c-441d-a640-4f66ef7f1b2f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinDataIntersectionEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinDataIntersectionEx
req.alt-loc: ks.h
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

# KsPinDataIntersectionEx function



## -description
<p>The <b>KsPinDataIntersectionEx</b> function handles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565198">KSPROPERTY_PIN_DATAINTERSECTION</a> through a callback function.</p>


## -syntax

````
NTSTATUS KsPinDataIntersectionEx(
  _In_           PIRP                    Irp,
  _In_           PKSP_PIN                Pin,
  _Out_          PVOID                   Data,
  _In_           ULONG                   DescriptorsCount,
  _In_     const KSPIN_DESCRIPTOR        *Descriptor,
  _In_           ULONG                   DescriptorSize,
  _In_opt_       PFNKSINTERSECTHANDLEREX IntersectHandler,
  _In_opt_       PVOID                   HandlerContext
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP that describes the property request.</p>
</dd>

### -param <i>Pin</i> [in]

<dd>
<p>Specifies the specific property that is being queried.</p>
</dd>

### -param <i>Data</i> [out]

<dd>
<p>Specifies the pin property-specific data.</p>
</dd>

### -param <i>DescriptorsCount</i> [in]

<dd>
<p>Specifies the number of descriptor structures.</p>
</dd>

### -param <i>Descriptor</i> [in]

<dd>
<p>Specifies the pointer to the list of pin information structures.</p>
</dd>

### -param <i>DescriptorSize</i> [in]

<dd>
<p>Size of the descriptor structures, in bytes.</p>
</dd>

### -param <i>IntersectHandler</i> [in, optional]

<dd>
<p>Contains the optional minidriver-defined <a href="stream.kstrintersecthandlerex">KStrIntersectHandlerEx</a> callback function to compare data ranges.</p>
</dd>

### -param <i>HandlerContext</i> [in, optional]

<dd>
<p>Optional context that is supplied to the handler.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS; otherwise, an error specific to the property that is being handled.</p>

## -remarks
<p><b>KsPinDataIntersectionEx</b> is very similar to <b>KsPinDataIntersection</b>, except for some of the following slight differences:</p>

<p>In <b>KsPinDataIntersectionEx</b>, the size of the descriptor is passed, a feature that allows extended descriptors.</p>

<p>The data intersection callback function is prototyped differently in the extended version (NTSTATUS Callback (<i>Context</i>, <i>Irp</i>, <i>Pin</i>, <i>DataRange</i>, <i>MatchingDataRange</i>, <i>DataBufferSize</i>, <i>Data</i>, <i>DataSize</i>)) versus <b>KsPinDataIntersection</b> (NTSTATUS Callback (<i>Irp</i>, <i>Pin</i>, <i>DataRange</i>, <i>Data</i>)).</p>

<p>The output buffer (<i>Data</i>) length is passed as a parameter to the data intersection callback function (<i>DataBufferSize</i>) rather than being extracted from the current I/O stack location.</p>

<p>The data intersection callback function is passed a <i>Context</i> parameter (the same <i>Context</i> parameter passed to <b>KsPinDataIntersectionEx</b>).</p>

<p>The size of the resultant format is passed back in <i>DataSize</i> instead of <i>Irp</i>-&gt;IoStatus.Information.</p>

<p>These differences excepted, <b>KsPinDataIntersection</b> and <b>KsPinDataIntersectionEx</b> operate similarly.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.kstrintersecthandlerex">KStrIntersectHandlerEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinDataIntersectionEx function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
