---
UID : NS:wmistr._WNODE_HEADER
title : _WNODE_HEADER
author : windows-driver-content
description : The WNODE_HEADER structure is the first member of all other WNODE_XXX structures. It contains information common to all such structures.
old-location : kernel\wnode_header.htm
old-project : kernel
ms.assetid : a895f048-b111-4ccc-8466-fe9b169a2f95
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _WNODE_HEADER, *PWNODE_HEADER, WNODE_HEADER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wmistr.h
req.include-header : Wmistr.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WNODE_HEADER
req.alt-loc : wmistr.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL (see Remarks section)
req.typenames : "*PWNODE_HEADER, WNODE_HEADER"
req.product : Windows 10 or later.
---

# _WNODE_HEADER structure
The <b>WNODE_HEADER</b> structure is the first member of all other <b>WNODE_<i>XXX</i></b> structures. It contains information common to all such structures.

## Syntax
````
typedef struct _WNODE_HEADER {
  ULONG BufferSize;
  ULONG ProviderId;
  union {
    ULONG64 HistoricalContext;
    struct {
      ULONG Version;
      ULONG Linkage;
    };
  };
  union {
    ULONG         CountLost;
    HANDLE        KernelHandle;
    LARGE_INTEGER TimeStamp;
  };
  GUID  Guid;
  ULONG ClientContext;
  ULONG Flags;
} WNODE_HEADER, *PWNODE_HEADER;
````

## Members

        
            `BufferSize`

            This member specifies the size, in bytes, of the nonpaged buffer to receive any <b>WNODE_<i>XXX</i></b> data to be returned, including this <b>WNODE_HEADER</b> structure, additional members of a <b>WNODE_<i>XXX</i></b> structure of the type indicated by <b>Flags</b>, and any WMI- or driver-determined data that accompanies that structure.
        
            `ClientContext`

            This member stores the clock type for the session. Possible values are included in the following table. 

<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
1

</td>
<td>
Performance counter value (also called QPC, QueryPerformanceCounter, or PerfCounter)

</td>
</tr>
<tr>
<td>
2

</td>
<td>
System timer

</td>
</tr>
<tr>
<td>
3

</td>
<td>
CPU cycle

</td>
</tr>
</table>
        
            `Flags`

            This member indicates the type of <b>WNODE_<i>XXX</i></b> structure that contains the WNODE_HEADER structure:
        
            `Guid`

            This member indicates the GUID that represents the data block associated with the <b>WNODE_<i>XXX</i></b> to be returned.
        
            `ProviderId`

            If <b>Flags</b> is set to WNODE_FLAG_EVENT_ITEM or WNODE_FLAG_EVENT_REFERENCE, <b>ProviderId</b> should contain the ID of the WMI provider associated with the device object. You can obtain the <b>ProviderId</b> value by calling <a href="..\wdm\nf-wdm-iowmideviceobjecttoproviderid.md">IoWMIDeviceObjectToProviderId</a>. If <b>Flags</b> is set to any other value, this member is reserved.

    ## Remarks
        In an <b>IRP_MN_CHANGE_<i>XXX</i></b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550868">IRP_MN_EXECUTE_METHOD</a> request, <b>BufferSize</b> in the IRP indicates the maximum size in bytes of the output buffer, while <b>BufferSize</b> in the input <b>WNODE_HEADER</b> for such a request indicates the size, in bytes, of the input data in the buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wmistr.h (include Wmistr.h) |

    ## See Also

        <dl>
<dt>
<a href="..\wdm\nf-wdm-iowmiwriteevent.md">IoWMIWriteEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iowmideviceobjecttoproviderid.md">IoWMIDeviceObjectToProviderId</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kequerysystemtime.md">KeQuerySystemTime</a>
</dt>
<dt>
<a href="..\wmistr\ns-wmistr-tagwnode_all_data.md">WNODE_ALL_DATA</a>
</dt>
<dt>
<a href="..\wmistr\ns-wmistr-tagwnode_event_item.md">WNODE_EVENT_ITEM</a>
</dt>
<dt>
<a href="..\wmistr\ns-wmistr-tagwnode_event_reference.md">WNODE_EVENT_REFERENCE</a>
</dt>
<dt>
<a href="..\wmistr\ns-wmistr-tagwnode_method_item.md">WNODE_METHOD_ITEM</a>
</dt>
<dt>
<a href="..\wmistr\ns-wmistr-tagwnode_single_instance.md">WNODE_SINGLE_INSTANCE</a>
</dt>
<dt>
<a href="..\wmistr\ns-wmistr-tagwnode_single_item.md">WNODE_SINGLE_ITEM</a>
</dt>
<dt>
<a href="..\wmistr\ns-wmistr-tagwnode_too_small.md">WNODE_TOO_SMALL</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20WNODE_HEADER structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>