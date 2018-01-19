---
UID : NS:pepfx._PEP_ACPI_EXTENDED_ADDRESS
title : _PEP_ACPI_EXTENDED_ADDRESS
author : windows-driver-content
description : The PEP_ACPI_EXTENDED_ADDRESS structure is used to report resource usage in the address space such as memory and IO.
old-location : kernel\pep_acpi_extended_address.htm
old-project : kernel
ms.assetid : E784765E-E346-4D57-B334-D0A0A823DAA8
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _PEP_ACPI_EXTENDED_ADDRESS, *PPEP_ACPI_EXTENDED_ADDRESS, PEP_ACPI_EXTENDED_ADDRESS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : pepfx.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Supported starting with Windows 10.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PEP_ACPI_EXTENDED_ADDRESS
req.alt-loc : pepfx.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PPEP_ACPI_EXTENDED_ADDRESS, PEP_ACPI_EXTENDED_ADDRESS"
---

# _PEP_ACPI_EXTENDED_ADDRESS structure
The <b>PEP_ACPI_EXTENDED_ADDRESS</b> structure is used to report resource usage in the address space such as memory and IO.

## Syntax
````
typedef struct _PEP_ACPI_EXTENDED_ADDRESS {
  PEP_ACPI_RESOURCE_TYPE  Type;
  PEP_ACPI_RESOURCE_FLAGS Flags;
  UCHAR                   ResourceFlags;
  UCHAR                   GeneralFlags;
  UCHAR                   TypeSpecificFlags;
  UCHAR                   RevisionId;
  UCHAR                   Reserved;
  ULONGLONG               Granularity;
  ULONGLONG               MinimumAddress;
  ULONGLONG               MaximumAddress;
  ULONGLONG               TranslationAddress;
  ULONGLONG               AddressLength;
  ULONGLONG               TypeAttribute;
  PUNICODE_STRING         DescriptorName;
} PEP_ACPI_EXTENDED_ADDRESS, *PPEP_ACPI_EXTENDED_ADDRESS;
````

## Members

        
            `AddressLength`

            The address length.
        
            `DescriptorName`

            The name of this resource descriptor.
        
            `Flags`

            A <a href="..\pepfx\ns-pepfx-_pep_acpi_resource_flags.md">PEP_ACPI_RESOURCE_FLAGS</a> structure describing this resource.
        
            `GeneralFlags`

            A value containing the bit flags that are common to all resource types. 

<table>
<tr>
<th>Bit(s)</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Granularity`

            A bit mask indicating which bits have been decoded.
        
            `MaximumAddress`

            The maximum starting address. For bridges that translate addresses, this is the address space
on the secondary side of the bridge.
        
            `MinimumAddress`

            The minimum starting address. For bridges that translate addresses, this is the address space on the secondary side of the bridge.
        
            `Reserved`

            
        
            `ResourceFlags`

            Indicates the type of resource this structure describes.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
        
            `RevisionId`

            Indicates the revision of the extended address space descriptor detailed by this structure. For ACPI 3.0, this value is 1.
        
            `TranslationAddress`

            For bridges that translate addresses across the bridge, this is the
address on the primary side.
        
            `Type`

            A <a href="..\pepfx\ne-pepfx-_pep_acpi_resource_type.md">PEP_ACPI_RESOURCE_TYPE</a> enumeration value describing this resource.
        
            `TypeAttribute`

            Indicates attributes that are specific to the resource type that is specified in the <b>ResourceFlags</b> member. If <b>ResourceFlags</b> is zero, this value is zero, otherwise the meaning of the value can be found in the <i>UEFI Specification</i> in the section titled <b>GetMemoryMap()</b>.
        
            `TypeSpecificFlags`

            The value of this member is dependent on the value in <b>ResourceFlags</b> member. The flags for each resource type are described in the tables below.


Memory Resource (<b>ResourceFlags</b> = <b>0</b>)



<table>
<tr>
<th>Bit(s)</th>
<th>Meaning</th>
</tr>
<tr>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pepfx.h |