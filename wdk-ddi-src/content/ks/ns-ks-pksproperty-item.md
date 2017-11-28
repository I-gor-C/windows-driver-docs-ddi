---
UID: NS.ks.PKSPROPERTY_ITEM
title: PKSPROPERTY_ITEM
author: windows-driver-content
description: Drivers use the KSPROPERTY_ITEM structure to describe how they support a property in a property set.
old-location: stream\ksproperty_item.htm
old-project: stream
ms.assetid: 58530a72-6e07-44f5-9d7d-04bc37ff1ec9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPROPERTY_ITEM, KSPROPERTY_ITEM, *PKSPROPERTY_ITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_ITEM
req.alt-loc: ks.h
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

# PKSPROPERTY_ITEM structure



## -description
<p>Drivers use the KSPROPERTY_ITEM structure to describe how they support a property in a property set.</p>


## -syntax

````
typedef struct {
  ULONG                   PropertyId;
  union {
    PFNKSHANDLER GetPropertyHandler;
    BOOLEAN      GetSupported;
  };
  ULONG                   MinProperty;
  ULONG                   MinData;
  union {
    PFNKSHANDLER SetPropertyHandler;
    BOOLEAN      SetSupported;
  };
  const KSPROPERTY_VALUES *Values;
  ULONG                   RelationsCount;
  const KSPROPERTY        *Relations;
  PFNKSHANDLER            SupportHandler;
  ULONG                   SerializedSize;
} KSPROPERTY_ITEM, *PKSPROPERTY_ITEM;
````


## -struct-fields
<dl>

### -field <b>PropertyId</b>

<dd>
<p>Specifies the ID of the property being described.</p>
</dd>

### -field <b>GetPropertyHandler</b>

<dd>
<p>Pointer to a minidriver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff567177">KStrGetPropertyHandler</a>. If <b>NULL</b>, the property cannot be read. This member is used only by drivers that use the AVStream or Stream class interfaces.</p>
</dd>

### -field <b>GetSupported</b>

<dd>
<p>Set to <b>TRUE</b> if this property supports get requests, <b>FALSE</b> if it does not. (The class driver fulfills the request through the SRB_GET_DEVICE_PROPERTY or SRB_GET_STREAM_PROPERTY requests.) This member is used only by minidrivers running under stream class. </p>
</dd>

### -field <b>MinProperty</b>

<dd>
<p>Specifies the minimum buffer length to hold the property identifier. This must be at least <b>sizeof</b>(<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>).</p>
</dd>

### -field <b>MinData</b>

<dd>
<p>Specifies the minimum buffer length to hold the data read from or written to this property.</p>
</dd>

### -field <b>SetPropertyHandler</b>

<dd>
<p>Pointer to a minidriver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff567200">KStrSetPropertyHandler</a>. If <b>NULL</b>, the property cannot be set. This member is used only by drivers that use the AVStream or Stream class interfaces.</p>
</dd>

### -field <b>SetSupported</b>

<dd>
<p>Set to <b>TRUE</b> if this property supports set requests, <b>FALSE</b> if it does not. (The class driver fulfills the request through the SRB_SET_DEVICE_PROPERTY or SRB_SET_STREAM_PROPERTY requests.)</p>
</dd>

### -field <b>Values</b>

<dd>
<p>Pointer to a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff565966">KSPROPERTY_VALUES</a>. Specifies the acceptable and/or default values for the property. These are the same as the values reported by a driver in response to an IOCTL_KS_PROPERTY request with the KSPROPERTY_TYPE_BASICSUPPORT and KSPROPERTY_TYPE_DEFAULTVALUES flags set.</p>
</dd>

### -field <b>RelationsCount</b>

<dd>
<p>Specifies the number of entries in the array pointed to by the <b>Relations</b> member.</p>
</dd>

### -field <b>Relations</b>

<dd>
<p>Points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structures representing properties related to this one. Two properties are considered related if changing one property may affect the value of the other property. The <b>Flags</b> member of each entry is unused.</p>
</dd>

### -field <b>SupportHandler</b>

<dd>
<p>Provide this member only if implementing your own format for raw serialization or raw unserialization. Basic support queries, range queries, and relations queries are automatically handled by AVStream, which returns the relevant values from other members of this KSPROPERTY_ITEM structure.</p>
</dd>

### -field <b>SerializedSize</b>

<dd>
<p>Specifies the size of the property when serialized in a KSPROPERTY_TYPE_SERIALIZESET request. This should be zero if the property cannot be serialized. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> for more information.</p>
</dd>
</dl>

## -remarks
<p>Stream class minidrivers use KSPROPERTY_ITEM to describe to the client how to fulfill property requests on each property within a set. Handling for the property set as a whole is specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565617">KSPROPERTY_SET</a> structure, which contains pointers to arrays of KSPROPERTY_ITEM structures.</p>

<p>The stream class driver handles property requests on behalf of the minidriver. When the stream class driver requires more information from the minidriver, it passes an SRB_XXX request to one of the minidriver's <b>StrMiniReceiveXXXRequest</b> routines. The stream class driver handles the different request types as listed in the following table.</p>

<p>KSPROPERTY_TYPE_GET</p>

<p>If <b>GetSupported</b> is <b>TRUE</b>, the stream class driver submits an <a href="https://msdn.microsoft.com/library/windows/hardware/ff568170">SRB_GET_DEVICE_PROPERTY</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568175">SRB_GET_STREAM_PROPERTY</a> request to the appropriate minidriver <b>StrMiniReceiveXXXRequest</b> routine.</p>

<p>KSPROPERTY_TYPE_SET</p>

<p>If <b>SetSupported</b> is <b>TRUE</b>, the stream class driver submits an <a href="https://msdn.microsoft.com/library/windows/hardware/ff568204">SRB_SET_DEVICE_PROPERTY</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568207">SRB_SET_STREAM_PROPERTY</a> request to the appropriate minidriver <b>StrMiniReceiveXXXRequest</b> routine.</p>

<p>KSPROPERTY_TYPE_BASICSUPPORT</p>

<p>The stream class driver uses KSPROPERTY_ITEM to obtain the information necessary to fulfill this request. For example, to specify the data type and permitted ranges of the property data, they each use the <b>Values</b> member of this structure.</p>

<p>KSPROPERTY_TYPE_SETSUPPORT</p>

<p>The stream class driver completes the property request IRP as STATUS_SUCCESS only if the driver supplies an entry for the property set within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff565617">KSPROPERTY_SET</a> structure.</p>

<p>KSPROPERTY_TYPE_DEFAULTVALUES</p>

<p>The stream class driver uses the <b>Values</b> member of this structure to determine the default values for the property data.</p>

<p>KSPROPERTY_TYPE_RELATIONS</p>

<p>The stream class driver uses the <b>Relations</b> member to determine what properties are related to this property.</p>

<p> </p>

<p>If the client specifies KSPROPERTY_TYPE_DEFAULTVALUES, the driver uses the data buffer to return a description of its value type, including possibly its allowed range and default value. This flag is similar in result to KSPROPERTY_TYPE_BASICSUPPORT, except that any values returned are those that have been marked with KSPROPERTY_MEMBER_FLAG_DEFAULT in the <b>Flags</b> member of the structure <a href="https://msdn.microsoft.com/library/windows/hardware/ff565189">KSPROPERTY_MEMBERSHEADER</a>.</p>

<p>For more information, see <a href="NULL">KS Properties</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565617">KSPROPERTY_SET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568170">SRB_GET_DEVICE_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568175">SRB_GET_STREAM_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568204">SRB_SET_DEVICE_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568207">SRB_SET_STREAM_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565966">KSPROPERTY_VALUES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_ITEM structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
