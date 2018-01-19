---
UID : NS:wdm._IO_RESOURCE_DESCRIPTOR
title : _IO_RESOURCE_DESCRIPTOR
author : windows-driver-content
description : The IO_RESOURCE_DESCRIPTOR structure describes a range of raw hardware resources, of one type, that can be used by a device. An array of IO_RESOURCE_DESCRIPTOR structures is contained within each IO_RESOURCE_LIST structure.
old-location : kernel\io_resource_descriptor.htm
old-project : kernel
ms.assetid : 03e3a656-c691-4aff-bcc8-4e0bc8390fd7
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _IO_RESOURCE_DESCRIPTOR, *PIO_RESOURCE_DESCRIPTOR, IO_RESOURCE_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IO_RESOURCE_DESCRIPTOR
req.alt-loc : Wdm.h
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
req.typenames : "*PIO_RESOURCE_DESCRIPTOR, IO_RESOURCE_DESCRIPTOR"
req.product : Windows 10 or later.
---

# _IO_RESOURCE_DESCRIPTOR structure
The <b>IO_RESOURCE_DESCRIPTOR</b> structure describes a range of raw hardware resources, of one type, that can be used by a device. An array of <b>IO_RESOURCE_DESCRIPTOR</b> structures is contained within each <a href="..\wdm\ns-wdm-_io_resource_list.md">IO_RESOURCE_LIST</a> structure.

## Syntax
````
typedef struct _IO_RESOURCE_DESCRIPTOR {
  UCHAR  Option;
  UCHAR  Type;
  UCHAR  ShareDisposition;
  UCHAR  Spare1;
  USHORT Flags;
  USHORT Spare2;
  union {
    struct {
      ULONG            Length;
      ULONG            Alignment;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } port;
    struct {
      ULONG            Length;
      ULONG            Alignment;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Memory;
    struct {
      ULONG             MinimumVector;
      ULONG             MaximumVector;
#if defined(NT_PROCESSOR_GROUPS)
      IRQ_DEVICE_POLICY AffinityPolicy;
      USHORT            Group;
#else 
      IRQ_DEVICE_POLICY AffinityPolicy;
#endif 
      IRQ_PRIORITY      PriorityPolicy;
      KAFFINITY         TargetedProcessors;
    } Interrupt;
    struct {
      ULONG MinimumChannel;
      ULONG MaximumChannel;
    } Dma;
    struct {
      ULONG RequestLine;
      ULONG Reserved;
      ULONG Channel;
      ULONG TransferWidth;
    } DmaV3;
    struct {
      ULONG            Length;
      ULONG            Alignment;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Generic;
    struct {
      ULONG Data[3];
    } DevicePrivate;
    struct {
      ULONG Length;
      ULONG MinBusNumber;
      ULONG MaxBusNumber;
      ULONG Reserved;
    } BusNumber;
    struct {
      ULONG Priority;
      ULONG Reserved1;
      ULONG Reserved2;
    } ConfigData;
    struct {
      ULONG            Length40;
      ULONG            Alignment40;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Memory40;
    struct {
      ULONG            Length48;
      ULONG            Alignment48;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Memory48;
    struct {
      ULONG            Length64;
      ULONG            Alignment64;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Memory64;
    struct {
      UCHAR Class;
      UCHAR Type;
      UCHAR Reserved1;
      UCHAR Reserved2;
      ULONG IdLowPart;
      ULONG IdHighPart;
    } Connection;
  } u;
} IO_RESOURCE_DESCRIPTOR, *PIO_RESOURCE_DESCRIPTOR;
````

## Members

        
            `Flags`

            Contains bit flags that are specific to the resource type. The following table shows the flags that are valid if <b>Type</b> = <b>CmResourceTypeInterrupt.</b>

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Option`

            Specifies whether this resource description is required, preferred, or alternative. One of the following values must be used:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `ShareDisposition`

            Indicates whether the described resource can be shared. For a list of valid values, see the <b>ShareDisposition</b> member of the <a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.
        
            `Spare1`

            
        
            `Spare2`

            
        
            `Type`

            Identifies the resource type. For a list of valid values, see the <b>Type</b> member of the <a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.
        
            `u`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

    ## See Also

        <dl>
<dt>
<a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm-_io_resource_requirements_list.md">IO_RESOURCE_REQUIREMENTS_LIST</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm-_io_resource_list.md">IO_RESOURCE_LIST</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioconnectinterrupt.md">IoConnectInterrupt</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_RESOURCE_DESCRIPTOR structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>