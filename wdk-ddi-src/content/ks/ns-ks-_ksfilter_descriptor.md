---
UID : NS:ks._KSFILTER_DESCRIPTOR
title : _KSFILTER_DESCRIPTOR
author : windows-driver-content
description : The KSFILTER_DESCRIPTOR structure describes the characteristics of a filter created by a given filter factory.
old-location : stream\ksfilter_descriptor.htm
old-project : stream
ms.assetid : c9e3c1ea-a8c9-45db-a31c-7f8e95cf6b2b
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _KSFILTER_DESCRIPTOR, *PKSFILTER_DESCRIPTOR, KSFILTER_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSFILTER_DESCRIPTOR
req.alt-loc : ks.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PKSFILTER_DESCRIPTOR, KSFILTER_DESCRIPTOR"
---

# _KSFILTER_DESCRIPTOR structure
The KSFILTER_DESCRIPTOR structure describes the characteristics of a filter created by a given filter factory.

## Syntax
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

## Members


    ## Remarks
        In laying out the filter descriptor, there are a number of macros that the caller may find useful. Instead of specifying count, size, and a table for pin descriptors, categories, node descriptors, and connections, there are a number of useful macros:

<b>DEFINE_KSFILTER_PIN_DESCRIPTORS</b>(<i>Table</i>)

Automatically inserts the number of items in table, the size of each item in the table, and the table of pin descriptors itself into the filter descriptor.

<b>DEFINE_KSFILTER_CATEGORIES</b>(<i>Table</i>)

Automatically inserts the number of categories in the table and the table itself into the filter descriptor.

<b>DEFINE_KSFILTER_CATEGORIES_NULL</b>

Automatically fills in the category members for a filter that defines no categories.

<b>DEFINE_KSFILTER_NODE_DESCRIPTORS</b>(<i>Table</i>)

Automatically inserts the number of items in the table, the size of each item in the table, and the table of node descriptors itself into the filter descriptor.

<b>DEFINE_KSFILTER_NODE_DESCRIPTORS_NULL</b>

Automatically fills in the node descriptor members for a filter that defines no topology nodes.

<b>DEFINE_KSFILTER_CONNECTIONS</b>(<i>Table</i>)

Automatically inserts the number of connections in the table and the table itself into the filter descriptor.

<b>DEFINE_KSFILTER_DEFAULT_CONNECTIONS</b>

Automatically fills in the connections table for a filter that defines no explicit connections.

If you do not use <b>DEFINE_KS_FILTER_PIN_DESCRIPTORS</b> to set <i>PinDescriptorSize</i>, then you must set <i>PinDescriptorSize</i> to <b>sizeof(KSPIN_DESCRIPTOR_EX)</b>.

Similarly, if you do not use <b>DEFINE_KS_FILTER_NODE_DESCRIPTORS</b> to set <i>NodeDescriptorSize</i>, then you must set <i>NodeDescriptorSize</i> to <b>sizeof(KSNODE_DESCRIPTOR)</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ks\ns-ks-_ksfilter_dispatch.md">KSFILTER_DISPATCH</a>
</dt>
<dt>
<a href="..\ks\ns-ks-_kspin_descriptor_ex.md">KSPIN_DESCRIPTOR_EX</a>
</dt>
<dt>
<a href="..\ks\ns-ks-_ksnode_descriptor.md">KSNODE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ks\ns-ks-kstopology_connection.md">KSTOPOLOGY_CONNECTION</a>
</dt>
<dt>
<a href="..\ks\ns-ks-kscomponentid.md">KSCOMPONENTID</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kscreatefilterfactory.md">KsCreateFilterFactory</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSFILTER_DESCRIPTOR structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>