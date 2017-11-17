---
UID: NS.ksmedia._DS3DVECTOR
title: DS3DVECTOR
author: windows-driver-content
description: The DS3DVECTOR structure contains three-dimensional position coordinates, position vector components, or velocity vector components.
old-location: audio\ds3dvector.htm
ms.assetid: 828bb255-4640-4508-866e-e3641ca05773
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DS3DVECTOR
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
ms.keywords: DS3DVECTOR, DS3DVECTOR, *PDS3DVECTOR
req.iface: 
---

# DS3DVECTOR structure



## -description
<p>The DS3DVECTOR structure contains three-dimensional position coordinates, position vector components, or velocity vector components.</p>


## -syntax

````
typedef struct _DS3DVECTOR {
  union {
    FLOAT x;
    FLOAT dvX;
  };
  union {
    FLOAT y;
    FLOAT dvY;
  };
  union {
    FLOAT z;
    FLOAT dvZ;
  };
} DS3DVECTOR, *PDS3DVECTOR;
````


## -struct-fields
<dl>

### -field <b>x</b>

<dd>
<p>Specifies the x-coordinate of the position.</p>
</dd>

### -field <b>dvX</b>

<dd>
<p>Specifies the x-component of the vector.</p>
</dd>

### -field <b>y</b>

<dd>
<p>Specifies the y-coordinate of the position.</p>
</dd>

### -field <b>dvY</b>

<dd>
<p>Specifies the y-component of the vector.</p>
</dd>

### -field <b>z</b>

<dd>
<p>Specifies the z-coordinate of the position.</p>
</dd>

### -field <b>dvZ</b>

<dd>
<p>Specifies the z-component of the vector.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537101">KSDS3D_BUFFER_ALL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537116">KSDS3D_LISTENER_ALL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537119">KSDS3D_LISTENER_ORIENTATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20DS3DVECTOR structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
