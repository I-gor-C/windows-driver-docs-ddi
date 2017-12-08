---
UID: NE.bthddi._ENUMERATOR_TYPE
title: ENUMERATOR_TYPE
author: windows-driver-content
description: The ENUMERATOR_TYPE enumeration type is used to determine whether the enumerated device is associated with a service or a protocol. The ENUMERATOR_TYPE enumeration is intended for internal use only and should not be used by profile drivers.
old-location: bltooth\enumerator_type.htm
old-project: bltooth
ms.assetid: 2f8ae260-3a4c-44a5-85b7-e3ebcf21522b
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ENUMERATOR_TYPE
req.alt-loc: bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
req.iface: IBidiSpl2
---

# ENUMERATOR_TYPE enumeration



## -description
<p>The ENUMERATOR_TYPE enumeration type is used to determine whether the enumerated device is associated
  with a service or a protocol. The ENUMERATOR_TYPE enumeration is intended for internal use only and should
  not be used by profile drivers.</p>


## -syntax

````
typedef enum _ENUMERATOR_TYPE { 
  ENUMERATOR_TYPE_PROTOCOL  = 0,
  ENUMERATOR_TYPE_SERVICE   = 1,
  ENUMERATOR_TYPE_MAX       = 2
} ENUMERATOR_TYPE, *PENUMERATOR_TYPE;
````


## -enum-fields
<dl>

### -field ENUMERATOR_TYPE_PROTOCOL

<dd>
<p>For internal use only. Do not use.</p>
</dd>

### -field ENUMERATOR_TYPE_SERVICE

<dd>
<p>This value should be specified for profile drivers. For more information about how this value is
     used, see 
     <a href="..\bthddi\ns-bthddi--bth-enumerator-info.md">BTH_ENUMERATOR_INFO</a>.</p>
</dd>

### -field ENUMERATOR_TYPE_MAX

<dd>
<p>For internal use only. Do not use.</p>
</dd>
</dl>

## -remarks
<p>A value from this enumeration is returned as the 
    <b>EnumeratorType</b> member of the 
    <a href="..\bthddi\ns-bthddi--bth-enumerator-info.md">BTH_ENUMERATOR_INFO</a> structure, which the 
    <a href="..\bthioctl\ni-bthioctl-ioctl-internal-bthenum-get-enuminfo.md">
    IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO</a> returns in its output buffer.</p>

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
<dt>Bthddi.h (include Bthddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\bthddi\ns-bthddi--bth-enumerator-info.md">BTH_ENUMERATOR_INFO</a>
</dt>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl-internal-bthenum-get-enuminfo.md">
   IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20ENUMERATOR_TYPE enumeration%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
