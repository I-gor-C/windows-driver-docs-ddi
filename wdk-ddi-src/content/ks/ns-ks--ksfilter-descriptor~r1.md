---
UID: NS.ks._KSFILTER_DESCRIPTOR~r1
title: KSFILTER_DESCRIPTOR
author: windows-driver-content
description: The KSFILTER_DESCRIPTOR structure describes the characteristics of a filter created by a given filter factory.
old-location: stream\ksfilter_descriptor.htm
old-project: stream
ms.assetid: c9e3c1ea-a8c9-45db-a31c-7f8e95cf6b2b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KSFILTER_DESCRIPTOR,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSFILTER_DESCRIPTOR
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

# KSFILTER_DESCRIPTOR structure



## -description
<p>The KSFILTER_DESCRIPTOR structure describes the characteristics of a filter created by a given filter factory.</p>


## -syntax

````
typedef struct _KSFILTER_DESCRIPTOR {
  const KSFILTER_DISPATCH     *Dispatch;
  const KSAUTOMATION_TABLE    *AutomationTable;
  ULONG                       Version;
  ULONG                       Flags;
  const GUID                  *ReferenceGuid;
  ULONG                       PinDescriptorsCount;
  ULONG                       PinDescriptorSize;
  const KSPIN_DESCRIPTOR_EX   *PinDescriptors;
  ULONG                       CategoriesCount;
  const GUID                  *Categories;
  ULONG                       NodeDescriptorsCount;
  ULONG                       NodeDescriptorSize;
  const KSNODE_DESCRIPTOR     *NodeDescriptors;
  ULONG                       ConnectionsCount;
  const KSTOPOLOGY_CONNECTION *Connections;
  const KSCOMPONENTID         *ComponentId;
} KSFILTER_DESCRIPTOR, *PKSFILTER_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Dispatch</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562554">KSFILTER_DISPATCH</a> structure for this type of filter. This member is optional and need only be provided by clients that wish to receive notifications about filter creations, deletions, and so on. Drivers that are interested in the processing of data (transforms) typically provide this dispatch table and a processing function. Providing a filter-processing function instead of individual pin-processing functions is what makes a driver filter-centric instead of pin-centric.</p>
</dd>

### -field <b>AutomationTable</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560990">KSAUTOMATION_TABLE</a> structure for this type of filter. The automation table is what describes the properties, methods, and events supported by this filter. This automation table is merged with the automation table supplied by AVStream for all filters. Should the client supply a property, method, or event handler already implemented by AVStream, the client's implementation supersedes AVStream's.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>This member specifies the version of the filter descriptor. This member should be set to KSFILTER_DESCRIPTOR_VERSION.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags describing the behavior of the filter. Specify flags using a bitwise OR, with the exception of KSFILTER_FLAG_CRITICAL_PROCESSING and KSFILTER_FLAG_HYPERCRITICAL_PROCESSING, which are mutually exclusive:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSFILTER_FLAG_DISPATCH_LEVEL_PROCESSING</p>
</td>
<td>
<p>Indicates that the filter processes at IRQL DISPATCH_LEVEL as opposed to PASSIVE_LEVEL. This applies to the filter process callback as described in <a href="https://msdn.microsoft.com/library/windows/hardware/ff562554">KSFILTER_DISPATCH</a>.</p>
</td>
</tr>
<tr>
<td>
<p>KSFILTER_FLAG_CRITICAL_PROCESSING</p>
</td>
<td>
<p>If asynchronous processing has been specified or if the system is running at PASSIVE_LEVEL and a process call comes in at DISPATCH_LEVEL, processing is done in a queued work item. This flag indicates that the work item should be placed on the critical work queue as opposed to the delayed work queue.</p>
</td>
</tr>
<tr>
<td>
<p>KSFILTER_FLAG_RECEIVE_ZERO_LENGTH_SAMPLES</p>
</td>
<td>
<p>Set this flag if a filter-centric filter needs to receive zero-length samples (stream headers with flags but no data). If this flag is not set, zero length samples are passed on to downstream pins, with automatic propagation of necessary flags. Note that this is identical to default behavior in DX8 and prior. If this happens, <i>these samples bypass the minidriver</i>. Set the <b>Terminate</b> flag in <a href="https://msdn.microsoft.com/library/windows/hardware/ff564256">KSPROCESSPIN</a> to "turn off" this flag. Also see <a href="NULL">Filter-Centric Processing</a>.</p>
</td>
</tr>
<tr>
<td>
<p>KSFILTER_FLAG_DENY_USERMODE_ACCESS</p>
</td>
<td>
<p>This flag prevents user-mode access to a specific filter and all pins instantiated on this filter.</p>
</td>
</tr>
<tr>
<td>
<p>KSFILTER_FLAG_HYPERCRITICAL_PROCESSING</p>
</td>
<td>
<p>If asynchronous processing has been specified or if the system is running at PASSIVE_LEVEL and a process call comes in at DISPATCH_LEVEL, AVStream processes a queued work item. This flag indicates that the work item should be placed on the hypercritical work queue as opposed to the delayed work queue or critical work queue.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ReferenceGuid</b>

<dd>
<p>A pointer to a GUID that is the binary representation of the Unicode reference string identifying this filter type. If multiple filter factories exist, each must have a unique GUID. Also note that other methods of supplying a reference string require that the filter descriptor be registered using <b>KsCreateFilterFactory</b>. The value specified in <b>ReferenceGuid</b> must match the filter-specific reference GUID in the driver's INF file. See <a href="NULL">Initializing an AVStream Minidriver</a>.</p>
</dd>

### -field <b>PinDescriptorsCount</b>

<dd>
<p>This member specifies the number of pin descriptors that are provided for this filter type in the <b>PinDescriptors</b> member. On Windows XP and later, <b>PinDescriptorsCount</b> may be zero if the driver creates pins dynamically.</p>
</dd>

### -field <b>PinDescriptorSize</b>

<dd>
<p>This member specifies the size of each individual descriptor in the descriptor table. This value must be a multiple of eight and must be at least <b>sizeof</b> (KSPIN_DESCRIPTOR_EX). Larger values allow client-specific descriptor information to be appended to pin descriptors. See additional information in Remarks.</p>
</dd>

### -field <b>PinDescriptors</b>

<dd>
<p>A pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a> structures that describe the pins supported by this filter type. If <b>PinDescriptorsCount</b> is zero, set this member to <b>NULL</b>..</p>
</dd>

### -field <b>CategoriesCount</b>

<dd>
<p>This member specifies the number of category GUIDs that are provided in the <b>Categories</b> member for this filter type. Zero is a legal value for this member.</p>
</dd>

### -field <b>Categories</b>

<dd>
<p>A pointer to an array of category GUIDs for this filter type. If required, a device interface is registered for each category. This member may be <b>null</b> if and only if <b>CategoriesCount</b> is zero.</p>
</dd>

### -field <b>NodeDescriptorsCount</b>

<dd>
<p>This member specifies the number of topology node descriptors provided in <b>NodeDescriptors</b>. Zero is a legal value for this member.</p>
</dd>

### -field <b>NodeDescriptorSize</b>

<dd>
<p>This member specifies the size in bytes of each individual descriptor in the descriptor table. This value must be a multiple of eight and at least <b>sizeof </b>(KSNODE_DESCRIPTOR). Larger values allow client-specific descriptor information to be appended to node descriptors. See additional information in Remarks.</p>
</dd>

### -field <b>NodeDescriptors</b>

<dd>
<p>A pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563473">KSNODE_DESCRIPTOR</a> structures describing the topology nodes for this filter type. This member may be <b>null</b> if and only if <b>NodeDescriptorsCount</b> is zero.</p>
</dd>

### -field <b>ConnectionsCount</b>

<dd>
<p>This member specifies the number of topology connections present in <b>Connections</b>. This member may be zero indicating that the default connection set is used. Using default connections means that the topology of the filter is described with a single topology node where each pin on the filter is connected to the corresponding ID on the topology node. The direction of each connection is determined by pin data flow.</p>
</dd>

### -field <b>Connections</b>

<dd>
<p>A pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff567148">KSTOPOLOGY_CONNECTION</a> structures present in this filter type. This member is optional; it may be <b>NULL</b> if and only if <b>ConnectionsCount</b> is zero (in which case, the default topology is used).</p>
</dd>

### -field <b>ComponentId</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561027">KSCOMPONENTID</a> structure for this filter type. This is used for the component ID property that provides identification information. This member is optional.</p>
</dd>
</dl>

## -remarks
<p>In laying out the filter descriptor, there are a number of macros that the caller may find useful. Instead of specifying count, size, and a table for pin descriptors, categories, node descriptors, and connections, there are a number of useful macros:</p>

<p><b>DEFINE_KSFILTER_PIN_DESCRIPTORS</b>(<i>Table</i>)</p>

<p>Automatically inserts the number of items in table, the size of each item in the table, and the table of pin descriptors itself into the filter descriptor.</p>

<p><b>DEFINE_KSFILTER_CATEGORIES</b>(<i>Table</i>)</p>

<p>Automatically inserts the number of categories in the table and the table itself into the filter descriptor.</p>

<p><b>DEFINE_KSFILTER_CATEGORIES_NULL</b></p>

<p>Automatically fills in the category members for a filter that defines no categories.</p>

<p><b>DEFINE_KSFILTER_NODE_DESCRIPTORS</b>(<i>Table</i>)</p>

<p>Automatically inserts the number of items in the table, the size of each item in the table, and the table of node descriptors itself into the filter descriptor.</p>

<p><b>DEFINE_KSFILTER_NODE_DESCRIPTORS_NULL</b></p>

<p>Automatically fills in the node descriptor members for a filter that defines no topology nodes.</p>

<p><b>DEFINE_KSFILTER_CONNECTIONS</b>(<i>Table</i>)</p>

<p>Automatically inserts the number of connections in the table and the table itself into the filter descriptor.</p>

<p><b>DEFINE_KSFILTER_DEFAULT_CONNECTIONS</b></p>

<p>Automatically fills in the connections table for a filter that defines no explicit connections.</p>

<p> </p>

<p>If you do not use <b>DEFINE_KS_FILTER_PIN_DESCRIPTORS</b> to set <i>PinDescriptorSize</i>, then you must set <i>PinDescriptorSize</i> to <b>sizeof(KSPIN_DESCRIPTOR_EX)</b>.</p>

<p>Similarly, if you do not use <b>DEFINE_KS_FILTER_NODE_DESCRIPTORS</b> to set <i>NodeDescriptorSize</i>, then you must set <i>NodeDescriptorSize</i> to <b>sizeof(KSNODE_DESCRIPTOR)</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562554">KSFILTER_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563473">KSNODE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567148">KSTOPOLOGY_CONNECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561027">KSCOMPONENTID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561650">KsCreateFilterFactory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSFILTER_DESCRIPTOR structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
