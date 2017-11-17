---
UID: NF.ksproxy.IKsPinFactory.KsPinFactory
title: IKsPinFactory::KsPinFactory
author: windows-driver-content
description: The KsPinFactory method retrieves the identifier of a pin factory.
old-location: stream\ikspinfactory_kspinfactory.htm
ms.assetid: 939ea77d-f194-4751-b02b-80d5e83c46f4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsPinFactory.KsPinFactory
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
ms.keywords: IKsPinFactory, KsPinFactory, IKsPinFactory::KsPinFactory
req.iface: IKsPinFactory
---

# IKsPinFactory::KsPinFactory method



## -description
<p>The <b>KsPinFactory</b> method retrieves the identifier of a pin factory. </p>


## -syntax

````
HRESULT KsPinFactory(
  [out] ULONG *PinFactory
);
````


## -parameters
<dl>

### -param <i>PinFactory</i> [out]

<dd>
<p>Pointer to a variable that receives the identifier of the pin factory.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

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
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559910">IKsPinFactory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPinFactory::KsPinFactory method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
