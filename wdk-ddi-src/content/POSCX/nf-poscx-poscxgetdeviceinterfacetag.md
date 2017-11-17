---
UID: NF.poscx.PosCxGetDeviceInterfaceTag
title: PosCxGetDeviceInterfaceTag
author: windows-driver-content
description: PosCxGetDeviceInterfaceTag returns the device interface tag that is set in PosCxOpen.
old-location: pos\poscxgetdeviceinterfacetag.htm
ms.assetid: CF54D922-8EEE-41CE-8CFC-0628756117BE
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: pos
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxGetDeviceInterfaceTag
req.alt-loc: poscx.h
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
ms.keywords: PosCxGetDeviceInterfaceTag
req.iface: 
req.product: Windows 10 or later.
---

# PosCxGetDeviceInterfaceTag function



## -description
<p>PosCxGetDeviceInterfaceTag returns the device interface tag that is set in <a href="https://msdn.microsoft.com/library/windows/hardware/mt593129">PosCxOpen</a>.</p>


## -syntax

````
ULONG PosCxGetDeviceInterfaceTag(
  _In_ WDFFILEOBJECT fileObject
);
````


## -parameters
<dl>

### -param <i>fileObject</i> [in]

<dd>
<p>      A handle to a framework file object that identifies the caller, usually acquired with <a href="https://msdn.microsoft.com/library/windows/hardware/ff549963">WdfRequestGetFileObject</a>.</p>
</dd>
</dl>

## -returns
<p>      The device interface tag value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Product</p>
</th>
<td width="70%">
<p>Windows 10 or later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt593129">PosCxOpen</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [pos\pos]:%20PosCxGetDeviceInterfaceTag function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
