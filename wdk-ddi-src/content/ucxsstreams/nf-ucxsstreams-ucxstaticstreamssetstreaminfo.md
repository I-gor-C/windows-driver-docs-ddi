---
UID: NF.ucxsstreams.UcxStaticStreamsSetStreamInfo
title: UcxStaticStreamsSetStreamInfo function
author: windows-driver-content
description: Sets stream information for each stream enabled by the client driver.
old-location: buses\_ucxstaticstreamssetstreaminfo.htm
old-project: UsbRef
ms.assetid: 40AE9327-ABB7-4A63-AC90-494E2BC26C08
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: UcxStaticStreamsSetStreamInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxsstreams.h
req.include-header: Ucxclass.h, Ucxstreams.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: UcxStaticStreamsSetStreamInfo
req.alt-loc: ucxsstreams.h
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
req.product: Windows 10 or later.
---

# UcxStaticStreamsSetStreamInfo function



## -description
Sets stream information for each stream enabled by the client driver.



## -syntax

````
inline void UcxStaticStreamsSetStreamInfo(
  [in] UCXSSTREAMS  StaticStreams,
  [in] PSTREAM_INFO StreamInfo
);
````


## -parameters

### -param StaticStreams [in]

                The handle to the Static Streams object just been created. 


### -param StreamInfo [in]

                A pointer to a <a href="buses._stream_info">STREAM_INFO</a> structure that contains static stream-related information.


## -returns
This method does not return a value.


## -remarks
The client driver must call this method from its implementation of the <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_static_streams_add.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD</a> event callback . 
    This method must be called for the number of streams on the endpoint. 

For a code example, see <a href="..\ucxendpoint\nc-ucxendpoint-evt_ucx_endpoint_static_streams_add.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD</a>.


## -requirements
<table>
<tr>
<th width="30%">
Minimum support

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ucxsstreams.h (include Ucxclass.h or Ucxstreams.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._ucxendpointcreate">UcxEndpointCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20UcxStaticStreamsSetStreamInfo method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

