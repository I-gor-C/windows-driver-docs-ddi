---
UID: NF.swenum.KsQuerySoftwareBusInterface
title: KsQuerySoftwareBusInterface
author: windows-driver-content
description: The KsQuerySoftwareBusInterface function creates a buffer from the paged pool and copies the reference string associated with the demand-load bus enumerator object's PDO into the buffer.
old-location: stream\ksquerysoftwarebusinterface.htm
ms.assetid: 2a4dd5a8-e9cc-4404-8031-5091ff2aa50d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: swenum.h
req.include-header: Swenum.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsQuerySoftwareBusInterface
req.alt-loc: swenum.h
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
ms.keywords: KsQuerySoftwareBusInterface
req.iface: 
req.product: Windows 10 or later.
---

# KsQuerySoftwareBusInterface function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KsQuerySoftwareBusInterface</b> function creates a buffer from the paged pool and copies the reference string associated with the demand-load bus enumerator object's PDO into the buffer. It is the caller's responsibility to free the buffer using <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>. </p>


## -syntax

````
NTSTATUS KsQuerySoftwareBusInterface(
  _In_  PDEVICE_OBJECT        PnpDeviceObject,
  _Out_ PBUS_INTERFACE_SWENUM BusInterface
);
````


## -parameters
<dl>

### -param <i>PnpDeviceObject</i> [in]

<dd>
<p>Pointer to the demand-load bus enumerator's device object.</p>
</dd>

### -param <i>BusInterface</i> [out]

<dd>
<p>Pointer to the demand-load bus enumerator's interface.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the request is handled. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>A minidriver can access this function through the <b>QueryReferenceString</b> member of the BUS_INTERFACE_SWENUM structure.</p>

<p>A minidriver can access this function through the <b>QueryReferenceString</b> member of the BUS_INTERFACE_SWENUM structure.</p>

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
<dt>Swenum.h (include Swenum.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557589">BUS_INTERFACE_SWENUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566763">KsReferenceSoftwareBusObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561678">KsDereferenceSoftwareBusObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsQuerySoftwareBusInterface function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
