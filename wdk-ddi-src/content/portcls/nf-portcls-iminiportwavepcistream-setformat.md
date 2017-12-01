---
UID: NF.portcls.IMiniportWavePciStream.SetFormat
title: IMiniportWavePciStream::SetFormat
author: windows-driver-content
description: The SetFormat method sets the KS data format of the wave stream.
old-location: audio\iminiportwavepcistream_setformat.htm
old-project: audio
ms.assetid: c8dfa58d-f38b-4ef1-9607-575191d8ddea
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportWavePciStream, SetFormat, IMiniportWavePciStream::SetFormat
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWavePciStream.SetFormat
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: IMiniportWavePciStream
---

# IMiniportWavePciStream::SetFormat method



## -description
<p>The <code>SetFormat</code> method sets the KS data format of the wave stream.</p>


## -syntax

````
NTSTATUS SetFormat(
  [in] PKSDATAFORMAT DataFormat
);
````


## -parameters
<dl>

### -param <i>DataFormat</i> [in]

<dd>
<p>Pointer to <a href="stream.ksdataformat">KSDATAFORMAT</a> structure that describes the new format of the stream.</p>
</dd>
</dl>

## -returns
<p><code>SetFormat</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The wave stream's initial format is specified in the <a href="audio.iminiportwavepci_newstream">IMiniportWavePci::NewStream</a> call that creates the stream. Following stream creation, the <code>SetFormat</code> call can change the stream's format from its initial setting.</p>

<p>For information about specifying wave stream formats, see <a href="NULL">Audio Data Formats and Data Ranges</a>.</p>

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
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iminiportwavepcistream.md">IMiniportWavePciStream</a>
</dt>
<dt>
<a href="stream.ksdataformat">KSDATAFORMAT</a>
</dt>
<dt>
<a href="audio.iminiportwavepci_newstream">IMiniportWavePci::NewStream</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWavePciStream::SetFormat method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
