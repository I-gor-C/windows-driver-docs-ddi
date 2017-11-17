---
UID: NF.strmini.StreamClassRegisterFilterWithNoKSPins
title: StreamClassRegisterFilterWithNoKSPins
author: windows-driver-content
description: The StreamClassRegisterFilterWithNoKSPins routine is used to register filter drivers with Microsoft DirectShow that have no kernel streaming pins and, therefore, do not stream in kernel mode.
old-location: stream\streamclassregisterfilterwithnokspins.htm
ms.assetid: f5ae426a-9d9d-4391-b87f-c4281dc9cadc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StreamClassRegisterFilterWithNoKSPins
req.alt-loc: Stream.lib,Stream.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Stream.lib
req.dll: 
req.irql: 
ms.keywords: StreamClassRegisterFilterWithNoKSPins
req.iface: 
req.product: Windows 10 or later.
---

# StreamClassRegisterFilterWithNoKSPins function



## -description
<p>The <b>StreamClassRegisterFilterWithNoKSPins</b> routine is used to register filter drivers with Microsoft DirectShow that have no kernel streaming pins and, therefore, do not stream in kernel mode. </p>


## -syntax

````
NTSTATUS StreamClassRegisterFilterWithNoKSPins(
  _In_           PDEVICE_OBJECT DeviceObject,
  _In_     const GUID           *InterfaceClassGUID,
  _In_           ULONG          PinCount,
  _In_           BOOL           *PinDirection,
  _In_           KSPIN_MEDIUM   *MediumList,
  _In_opt_       GUID           *CategoryList
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Points to the driver's device object.</p>
</dd>

### -param <i>InterfaceClassGUID</i> [in]

<dd>
<p>Specifies the interface class GUID to register.</p>
</dd>

### -param <i>PinCount</i> [in]

<dd>
<p>Specifies the number of pins on the filter.</p>
</dd>

### -param <i>PinDirection</i> [in]

<dd>
<p>Specifies a <i>PinCount</i>-sized array of Boolean values, one for each pin on the filter. The values indicate the pin direction for each pin. If <b>TRUE</b>, this pin is an output pin. If <b>FALSE</b>, the pin is an input pin.</p>
</dd>

### -param <i>MediumList</i> [in]

<dd>
<p>Specifies a <i>PinCount</i>-sized array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a> structures, one for each pin on the filter.</p>
</dd>

### -param <i>CategoryList</i> [in, optional]

<dd>
<p>If non-NULL, specifies an array of pin category GUIDs, one for each pin on the filter.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS on success, or the appropriate error code on failure.</p>

## -remarks


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
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Stream.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20StreamClassRegisterFilterWithNoKSPins routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
