---
UID: NS.ksmedia._KS_COLCON
title: KS_COLCON
author: windows-driver-content
description: The KS_COLCON structure is used to describe color and contrast settings.
old-location: stream\ks_colcon.htm
ms.assetid: 8328c1b1-e72d-4e34-b69e-e02b3f5850bf
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_COLCON
req.alt-loc: ksmedia.h
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
ms.keywords: KS_COLCON, KS_COLCON, *PKS_COLCON
req.iface: 
---

# KS_COLCON structure



## -description
<p>The KS_COLCON structure is used to describe color and contrast settings.</p>


## -syntax

````
typedef struct _KS_COLCON {
  UCHAR emph1col  :4;
  UCHAR emph2col  :4;
  UCHAR backcol  :4;
  UCHAR patcol  :4;
  UCHAR emph1con  :4;
  UCHAR emph2con  :4;
  UCHAR backcon  :4;
  UCHAR patcon  :4;
} KS_COLCON, *PKS_COLCON;
````


## -struct-fields
<dl>

### -field <b>emph1col</b>

<dd>
<p>Indicates </p>
</dd>

### -field <b>emph2col</b>

<dd>
<p>Indicates </p>
</dd>

### -field <b>backcol</b>

<dd>
<p>Indicates </p>
</dd>

### -field <b>patcol</b>

<dd>
<p>Indicates </p>
</dd>

### -field <b>emph1con</b>

<dd>
<p>Indicates </p>
</dd>

### -field <b>emph2con</b>

<dd>
<p>Indicates </p>
</dd>

### -field <b>backcon</b>

<dd>
<p>Indicates </p>
</dd>

### -field <b>patcon</b>

<dd>
<p>Indicates </p>
</dd>
</dl>

## -remarks
<p>The KS_COLCON structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565627">KSPROPERTY_SPHLI</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565627">KSPROPERTY_SPHLI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_COLCON structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
