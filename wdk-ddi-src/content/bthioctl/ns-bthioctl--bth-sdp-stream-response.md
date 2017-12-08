---
UID: NS.bthioctl._BTH_SDP_STREAM_RESPONSE
title: BTH_SDP_STREAM_RESPONSE
author: windows-driver-content
description: The BTH_SDP_STREAM_RESPONSE structure contains information about an SDP record.
old-location: bltooth\bth_sdp_stream_response.htm
old-project: bltooth
ms.assetid: 5b7db410-8d9c-4c3e-aaae-44f7d5b779a0
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: BTH_SDP_STREAM_RESPONSE, BTH_SDP_STREAM_RESPONSE, *PBTH_SDP_STREAM_RESPONSE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthioctl.h
req.include-header: Bthioctl.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTH_SDP_STREAM_RESPONSE
req.alt-loc: bthioctl.h
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
req.iface: 
---

# BTH_SDP_STREAM_RESPONSE structure



## -description
<p>The BTH_SDP_STREAM_RESPONSE structure contains information about an SDP record.</p>


## -syntax

````
typedef struct _BTH_SDP_STREAM_RESPONSE {
  ULONG requiredSize;
  ULONG responseSize;
  UCHAR response[1];
} BTH_SDP_STREAM_RESPONSE, *PBTH_SDP_STREAM_RESPONSE;
````


## -struct-fields
<dl>

### -field requiredSize

<dd>
<p>The size, in bytes, of the entire SDP record. This value can be useful if the output buffer is too
     small to hold the entire record.</p>
</dd>

### -field responseSize

<dd>
<p>The size, in bytes, of the raw SDP record stream that follows this structure.</p>
</dd>

### -field response

<dd>
<p>The first byte of the SDP record stream.</p>
</dd>
</dl>

## -remarks
<p>This structure is returned with a raw stream to the output buffer of the 
    <a href="..\bthioctl\ni-bthioctl-ioctl-bth-sdp-attribute-search.md">
    IOCTL_BTH_SDP_ATTRIBUTE_SEARCH</a> and 
    <a href="..\bthioctl\ni-bthioctl-ioctl-bth-sdp-service-attribute-search.md">
    IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH</a> IOCTLs.</p>

<p>The 
    <b>requiredSize</b> and 
    <b>responseSize</b> members are included in this structure because the raw SDP record stream does not
    contain these fields.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthioctl.h (include Bthioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl-bth-sdp-attribute-search.md">IOCTL_BTH_SDP_ATTRIBUTE_SEARCH</a>
</dt>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl-bth-sdp-service-attribute-search.md">
   IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BTH_SDP_STREAM_RESPONSE structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
