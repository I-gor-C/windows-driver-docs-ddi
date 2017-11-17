---
UID: NS.ndis._NDIS_CONFIGURATION_OBJECT
title: NDIS_CONFIGURATION_OBJECT
author: windows-driver-content
description: The NDIS_CONFIGURATION_OBJECT structure defines the attributes of a configuration object that an NDIS driver can pass to the NdisOpenConfigurationEx function.
old-location: netvista\ndis_configuration_object.htm
ms.assetid: 8fa80414-c87a-4f05-b99c-5153f08a0862
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_CONFIGURATION_OBJECT
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
ms.keywords: NDIS_CONFIGURATION_OBJECT, NDIS_CONFIGURATION_OBJECT, *PNDIS_CONFIGURATION_OBJECT
req.iface: 
---

# NDIS_CONFIGURATION_OBJECT structure



## -description
<p>The NDIS_CONFIGURATION_OBJECT structure defines the attributes of a configuration object that an NDIS
  driver can pass to the 
  <a href="https://msdn.microsoft.com/76539106-6d8d-4a80-9c74-a6a4ca37c40e">
  NdisOpenConfigurationEx</a> function.</p>


## -syntax

````
typedef struct _NDIS_CONFIGURATION_OBJECT {
  NDIS_OBJECT_HEADER Header;
  NDIS_HANDLE        NdisHandle;
  ULONG              Flags;
} NDIS_CONFIGURATION_OBJECT, *PNDIS_CONFIGURATION_OBJECT;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_CONFIGURATION_OBJECT structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_CONFIGURATION_OBJECT, the 
     <b>Revision</b> member to NDIS_CONFIGURATION_OBJECT_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_CONFIGURATION_OBJECT_REVISION_1.</p>
</dd>

### -field <b>NdisHandle</b>

<dd>
<p>An NDIS handle that the caller obtained during initialization.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of the following flags:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_CONFIG_FLAG_FILTER_INSTANCE_CONFIGURATION"></a><a id="ndis_config_flag_filter_instance_configuration"></a>NDIS_CONFIG_FLAG_FILTER_INSTANCE_CONFIGURATION

<dd>
<p>Set this flag if a monitoring filter driver must access the filter module configuration for a
       specific filter module when there are multiple filter modules configured over the same miniport
       adapter. Modifying filter drivers must not use this flag.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>To configuration parameters in the registry, an NDIS driver can use the NDIS_CONFIGURATION_OBJECT
    structure to define a configuration object and then call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975122">NdisOpenConfigurationEx</a> function
    to get a configuration handle.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975122">NdisOpenConfigurationEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_CONFIGURATION_OBJECT structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
