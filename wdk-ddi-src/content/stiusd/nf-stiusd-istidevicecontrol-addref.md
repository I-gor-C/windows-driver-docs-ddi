---
UID: NF.stiusd.IStiDeviceControl.AddRef
title: IStiDeviceControl::AddRef
author: windows-driver-content
description: The IStiDeviceControl::AddRef method increments the reference count for the IStiDeviceControl interface.
old-location: image\istidevicecontrol_addref.htm
old-project: image
ms.assetid: 8aa28efb-a030-4fed-b9f2-0e67ff1e7c9e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDeviceControl, AddRef, IStiDeviceControl::AddRef
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDeviceControl.AddRef
req.alt-loc: Stiusd.h
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
req.iface: IStiDeviceControl
req.product: Windows 10 or later.
---

# IStiDeviceControl::AddRef method



## -description
<p>The <b>IStiDeviceControl::AddRef</b> method increments the reference count for the <b>IStiDeviceControl</b> interface.</p>


## -syntax

````
HRESULT AddRef();
````


## -parameters


## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDeviceControl::AddRef</b> method should be called from within a user-mode still image minidriver's <a href="image.istiusd_initialize">IStiUSD::Initialize</a> method.</p>

<p>A still image minidriver receives an <b>IStiDeviceControl</b> interface pointer as an input argument to its <a href="image.istiusd_initialize">IStiUSD::Initialize</a> method.</p>

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
<dt>Stiusd.h (include Stiusd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.istidevicecontrol_release">IStiDeviceControl::Release</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiDeviceControl::AddRef method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
