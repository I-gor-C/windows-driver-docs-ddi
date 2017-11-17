---
UID: NF.ks.KsFastPropertyHandler
title: KsFastPropertyHandler
author: windows-driver-content
description: The KsFastPropertyHandler function handles fast property requests through IOCTL_KS_PROPERTY. It responds to all property identifiers defined by the sets that are also contained in the fast I/O list. This function can only be called at PASSIVE_LEVEL.
old-location: stream\ksfastpropertyhandler.htm
ms.assetid: 39a216f8-297d-45cc-9bec-4c0ee9941441
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
req.alt-api: KsFastPropertyHandler
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
ms.keywords: KsFastPropertyHandler
req.iface: 
---

# KsFastPropertyHandler function



## -description
<p>The <b>KsFastPropertyHandler</b> function handles fast property requests through IOCTL_KS_PROPERTY. It responds to all property identifiers defined by the sets that are also contained in the fast I/O list. This function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
KSDDKAPI BOOLEAN NTAPI KsFastPropertyHandler(void);
````


## -parameters


## -returns
<p>The <b>KsFastPropertyHandler</b> function returns <b>TRUE</b> if the request was handled, or <b>FALSE</b> if the request was not handled. If <b>FALSE</b> is returned, an IRP is generated. If the request was handled, the function sets the IoStatus-&gt;Information element, either through setting it to zero because of an internal error, or through a property handler setting it. The property handler also sets the IoStatus-&gt;Status field when the property is actually handled.</p>

<p>The <b>KsFastPropertyHandler</b> function returns <b>TRUE</b> if the request was handled, or <b>FALSE</b> if the request was not handled. If <b>FALSE</b> is returned, an IRP is generated. If the request was handled, the function sets the IoStatus-&gt;Information element, either through setting it to zero because of an internal error, or through a property handler setting it. The property handler also sets the IoStatus-&gt;Status field when the property is actually handled.</p>

<p>The <b>KsFastPropertyHandler</b> function returns <b>TRUE</b> if the request was handled, or <b>FALSE</b> if the request was not handled. If <b>FALSE</b> is returned, an IRP is generated. If the request was handled, the function sets the IoStatus-&gt;Information element, either through setting it to zero because of an internal error, or through a property handler setting it. The property handler also sets the IoStatus-&gt;Status field when the property is actually handled.</p>

## -remarks
<p>The owner of a property set can perform prefiltering or postfiltering of the property handling, as well as processing requests made through the fast I/O dispatch interface for device control. The <b>KsFastPropertyHandler</b> function is only used to process requests that can be fulfilled quickly.  The <i>Wait</i> parameter of the fast I/O function is not passed and is assumed to be <b>TRUE</b>. </p>

<p>The owner of a property set can perform prefiltering or postfiltering of the property handling, as well as processing requests made through the fast I/O dispatch interface for device control. The <b>KsFastPropertyHandler</b> function is only used to process requests that can be fulfilled quickly.  The <i>Wait</i> parameter of the fast I/O function is not passed and is assumed to be <b>TRUE</b>. </p>

<p>The owner of a property set can perform prefiltering or postfiltering of the property handling, as well as processing requests made through the fast I/O dispatch interface for device control. The <b>KsFastPropertyHandler</b> function is only used to process requests that can be fulfilled quickly.  The <i>Wait</i> parameter of the fast I/O function is not passed and is assumed to be <b>TRUE</b>. </p>

<p>The owner of a property set can perform prefiltering or postfiltering of the property handling, as well as processing requests made through the fast I/O dispatch interface for device control. The <b>KsFastPropertyHandler</b> function is only used to process requests that can be fulfilled quickly.  The <i>Wait</i> parameter of the fast I/O function is not passed and is assumed to be <b>TRUE</b>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564263">KsPropertyHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFastPropertyHandler function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
