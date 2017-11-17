---
UID: NF.ks.KsPinDataIntersection
title: KsPinDataIntersection
author: windows-driver-content
description: The KsPinDataIntersection function handles the KSPROPERTY_PIN_DATAINTERSECTION property through a callback function and performs much of the initial validation of the parameters that are passed.
old-location: stream\kspindataintersection.htm
ms.assetid: e4bf090d-35ec-42fd-8b6e-ce51734adba5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinDataIntersection
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsPinDataIntersection
req.iface: 
---

# KsPinDataIntersection function



## -description
<p>The <b>KsPinDataIntersection</b> function handles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565198">KSPROPERTY_PIN_DATAINTERSECTION</a> property through a callback function and performs much of the initial validation of the parameters that are passed. <b>KsPinDataIntersection</b> calls the minidriver-defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff567182">KStrIntersectHandler</a> callback function with each potential data range after matching it to the list of data ranges assigned to that pin factory.</p>


## -syntax

````
NTSTATUS KsPinDataIntersection(
  _In_            PIRP                  Irp ,
  _In_            PKSP_PIN              Pin ,
  _Out_opt_       PVOID                 Data ,
  _In_            ULONG                 DescriptorsCount ,
  _In_      const KSPIN_DESCRIPTOR      *Descriptor ,
  _In_            PFNKSINTERSECTHANDLER IntersectHandler 
);
````


## -parameters
<dl>

### -param <i>Irp </i> [in]

<dd>
<p>Specifies the IRP that describes the property request.</p>
</dd>

### -param <i>Pin </i> [in]

<dd>
<p>Specifies the specific property that is being queried.</p>
</dd>

### -param <i>Data </i> [out, optional]

<dd>
<p>Specifies the pin property-specific data.</p>
</dd>

### -param <i>DescriptorsCount </i> [in]

<dd>
<p>Specifies the number of descriptor structures.</p>
</dd>

### -param <i>Descriptor </i> [in]

<dd>
<p>Specifies the pointer to the list of pin information structures.</p>
</dd>

### -param <i>IntersectHandler </i> [in]

<dd>
<p>Specifies the minidriver-defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff567182">KStrIntersectHandler</a> callback function to compare a data range.</p>
</dd>
</dl>

## -returns
<p>The <b>KsPinDataIntersection</b> function returns STATUS_SUCCESS if a matching range is found, STATUS_NO_MATCH if no matching range was found, or an error specific to the property being handled. The minidriver-defined <i><u>KStrIntersectHandler</u></i> intersection handler provided to <b>KsPinDataIntersection</b> is called with each data range supplied by the caller until either a match is found or an error occurs.</p>

<p>Note that the minidriver-defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff567182">KStrIntersectHandler</a> callback function has its own set of return values.

</p>

## -remarks
<p>A match can occur under three conditions: if the major format of the range passed is a wildcard or matches a pin factory range, if the subformat is a wildcard or matches, and if the specifier is a wildcard or matches. Since the data range size may be variable, it is not validated beyond checking that it is at least the size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structure.</p>

<p>A match can occur under three conditions: if the major format of the range passed is a wildcard or matches a pin factory range, if the subformat is a wildcard or matches, and if the specifier is a wildcard or matches. Since the data range size may be variable, it is not validated beyond checking that it is at least the size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567182">KStrIntersectHandler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinDataIntersection function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
