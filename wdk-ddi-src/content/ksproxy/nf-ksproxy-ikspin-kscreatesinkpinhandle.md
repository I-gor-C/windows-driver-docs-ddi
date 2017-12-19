---
UID: NF.ksproxy.IKsPin.KsCreateSinkPinHandle
title: IKsPin::KsCreateSinkPinHandle method
author: windows-driver-content
description: The KsCreateSinkPinHandle method creates a pin handle and stores it in the KS pin object.
old-location: stream\ikspin_kscreatesinkpinhandle.htm
old-project: stream
ms.assetid: 68faba0a-8057-4259-b93d-c19899637356
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IKsPin, IKsPin::KsCreateSinkPinHandle, KsCreateSinkPinHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsPin.KsCreateSinkPinHandle
req.alt-loc: ksproxy.h
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
---

# IKsPin::KsCreateSinkPinHandle method



## -description
The <b>KsCreateSinkPinHandle</b> method creates a pin handle and stores it in the KS pin object. 



## -syntax

````
HRESULT KsCreateSinkPinHandle(
  [in] KSPIN_INTERFACE Interface,
  [in] KSPIN_MEDIUM    Medium
);
````


## -parameters

### -param Interface [in]

A type reference to a <a href="stream.kspin_interface">KSPIN_INTERFACE</a> structure for the interface that <b>KsCreateSinkPinHandle</b> negotiated for the created pin. 


### -param Medium [in]

A type reference to a <a href="stream.kspin_medium">KSPIN_MEDIUM</a> structure for the medium that <b>KsCreateSinkPinHandle</b> negotiated for the created pin. 


## -returns
Returns NOERROR if successful; otherwise, returns an error code.


## -remarks
Since the <b>KsCreateSinkPinHandle</b> method uses pass-by-reference variables, it is not necessary to pass pointers to KSPIN_INTERFACE and KSPIN_MEDIUM structures as arguments. 

After <b>KsCreateSinkPinHandle</b> has created a pin handle, you can retrieve the handle by calling the <a href="stream.iksobject_ksgetobjecthandle">IKsObject::KsGetObjectHandle</a> method.

This method is for proxy use and is not recommended for application use.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.iksobject_ksgetobjecthandle">IKsObject::KsGetObjectHandle</a>
</dt>
<dt>
<a href="stream.kspin_interface">KSPIN_INTERFACE</a>
</dt>
<dt>
<a href="stream.kspin_medium">KSPIN_MEDIUM</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin::KsCreateSinkPinHandle method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

