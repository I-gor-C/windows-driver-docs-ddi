---
UID: NS.ksmedia.PKSDATAFORMAT_DSOUND
title: PKSDATAFORMAT_DSOUND
author: windows-driver-content
description: The KSDATAFORMAT_DSOUND structure provides detailed information about a DirectSound audio stream.
old-location: audio\ksdataformat_dsound.htm
ms.assetid: 2b620e4f-8c26-479a-8b06-4e558b0813e5
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
req.alt-api: KSDATAFORMAT_DSOUND
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
ms.keywords: PKSDATAFORMAT_DSOUND, KSDATAFORMAT_DSOUND, *PKSDATAFORMAT_DSOUND
req.iface: 
---

# PKSDATAFORMAT_DSOUND structure



## -description
<p>The KSDATAFORMAT_DSOUND structure provides detailed information about a DirectSound audio stream.</p>


## -syntax

````
typedef struct {
  KSDATAFORMAT        DataFormat;
  KSDSOUND_BUFFERDESC BufferDesc;
} KSDATAFORMAT_DSOUND, *PKSDATAFORMAT_DSOUND;
````


## -struct-fields
<dl>

### -field <b>DataFormat</b>

<dd>
<p>Specifies the stream's data format. This member is a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a>.</p>
</dd>

### -field <b>BufferDesc</b>

<dd>
<p>Describes the DirectSound buffer. This member is a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537121">KSDSOUND_BUFFERDESC</a>.</p>
</dd>
</dl>

## -remarks
<p>In response to an input <i>DataRange</i> parameter that specifies a DirectSound format (see example in <a href="NULL">DirectSound Stream Data Range</a>), the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536764">IMiniport::DataRangeIntersection</a> method checks to see if the specified pin supports a compatible DirectSound format. If so, the method outputs a KSDATAFORMAT_DSOUND structure (see example in <a href="NULL">DirectSound Stream Data Format</a>) to the buffer that its <i>ResultantFormat</i> parameter points to.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561656">KSDATAFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537121">KSDSOUND_BUFFERDESC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536764">IMiniport::DataRangeIntersection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSDATAFORMAT_DSOUND structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
