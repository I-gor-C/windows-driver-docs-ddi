---
UID: NF.swenum.KsReferenceSoftwareBusObject
title: KsReferenceSoftwareBusObject
author: windows-driver-content
description: The KsReferenceSoftwareBusObject function increments the reference count of the demand-load bus enumerator object's PDO.
old-location: stream\ksreferencesoftwarebusobject.htm
ms.assetid: 56c7ce80-36da-4991-a640-f87b712f683e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: swenum.h
req.include-header: Swenum.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsReferenceSoftwareBusObject
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
ms.keywords: KsReferenceSoftwareBusObject
req.iface: 
req.product: Windows 10 or later.
---

# KsReferenceSoftwareBusObject function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KsReferenceSoftwareBusObject</b> function increments the reference count of the demand-load bus enumerator object's PDO. </p>


## -syntax

````
NTSTATUS KsReferenceSoftwareBusObject(
  _In_ KSDEVICE_HEADER Header
);
````


## -parameters
<dl>

### -param <i>Header</i> [in]

<dd>
<p>Pointer to the device header (extension) of the demand-load bus enumerator.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the request is handled. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>A minidriver can access this function through the <b>ReferenceDeviceObject</b> member of the BUS_INTERFACE_SWENUM structure.</p>

<p>The device object remains active and enumerated until the reference count returns to 0.</p>

<p>A minidriver can access this function through the <b>ReferenceDeviceObject</b> member of the BUS_INTERFACE_SWENUM structure.</p>

<p>The device object remains active and enumerated until the reference count returns to 0.</p>

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
<dt>Swenum.h (include Swenum.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557589">BUS_INTERFACE_SWENUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561678">KsDereferenceSoftwareBusObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566749">KsQuerySoftwareBusInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsReferenceSoftwareBusObject function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
