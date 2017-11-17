---
UID: NE.ntddsd.SDPROP_MEDIA_STATE
title: SDPROP_MEDIA_STATE
author: windows-driver-content
description: The SDPROP_MEDIA_STATE enumeration lists the values associated with the media states property.
old-location: sd\sdprop_media_state.htm
ms.assetid: b59fd639-f2e2-4765-bcc7-01934df3a0bc
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: SD
req.header: ntddsd.h
req.include-header: Ntddsd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SDPROP_MEDIA_STATE
req.alt-loc: ntddsd.h
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
ms.keywords: STORAGE_DIAGNOSTIC_MP_REQUEST, STORAGE_DIAGNOSTIC_MP_REQUEST, *PSTORAGE_DIAGNOSTIC_MP_REQUEST
req.iface: 
---

# SDPROP_MEDIA_STATE enumeration



## -description
<p>The SDPROP_MEDIA_STATE enumeration lists the values associated with the media states property.</p>


## -syntax

````
typedef enum  { 
  SDPMS_NO_MEDIA        = 0,
  SDPMS_MEDIA_INSERTED  = 1
} SDPROP_MEDIA_STATE;
````


## -enum-fields
<dl>

### -field <a id="SDPMS_NO_MEDIA"></a><a id="sdpms_no_media"></a><b>SDPMS_NO_MEDIA</b>

<dd>
<p>Indicates that the media is not present.</p>
</dd>

### -field <a id="SDPMS_MEDIA_INSERTED"></a><a id="sdpms_media_inserted"></a><b>SDPMS_MEDIA_INSERTED</b>

<dd>
<p>Indicates that the media is inserted.</p>
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
<dt>Ntddsd.h (include Ntddsd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/09b30bf0-fe85-4ad5-bd3e-113ed3a093ac">SDBUS_REQUEST_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537909">SdBusSubmitRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537914">SdBusSubmitRequestAsync</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SD\buses]:%20SDPROP_MEDIA_STATE enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
