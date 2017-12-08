---
UID: NF.pepfx.PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE
title: PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure.
old-location: kernel\pep_acpi_initialize_extended_io_resource.htm
old-project: kernel
ms.assetid: 95464DE1-221A-4053-B124-4CFD44557CD3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE
req.alt-loc: pepfx.h
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

# PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function



## -description
<p>The <b>PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="..\pepfx\ns-pepfx--pep-acpi-extended-address.md">PEP_ACPI_EXTENDED_ADDRESS</a> structure.</p>


## -syntax

````
FORCEINLINE VOID PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE(
  _In_  BOOLEAN            ResourceUsage,
  _In_  UCHAR              Decode,
  _In_  BOOLEAN            IsMinFixed,
  _In_  BOOLEAN            IsMaxFixed,
  _In_  UCHAR              ISARanges,
  _In_  ULONGLONG          AddressGranularity,
  _In_  ULONGLONG          AddressMinimum,
  _In_  ULONGLONG          AddressMaximum,
  _In_  ULONGLONG          AddressTranslation,
  _In_  ULONGLONG          RangeLength,
  _In_  ULONGLONG          TypeSpecificAttributes,
  _In_  PUNICODE_STRING    DescriptorName,
  _In_  BOOLEAN            TranslationTypeNonStatic,
  _In_  BOOLEAN            TanslationSparseDensity,
  _Out_ PPEP_ACPI_RESOURCE Resource
);
````


## -parameters
<dl>

### -param ResourceUsage [in]

<dd>
<p>This parameter is copied into the <b>GeneralFlags</b> member of the initialized <a href="..\pepfx\ns-pepfx--pep-acpi-extended-address.md">PEP_ACPI_EXTENDED_ADDRESS</a> structure.</p>
</dd>

### -param Decode [in]

<dd>
<p>When set, indicates that this bridge subtractively decodes the address. This applies to top level bridges only. </p>
<p>When not set, indicates that this bridge positively decodes this address.</p>
</dd>

### -param IsMinFixed [in]

<dd>
<p>When set, indicates that the minimum address is fixed.</p>
</dd>

### -param IsMaxFixed [in]

<dd>
<p>When set, indicates that the maximum address is fixed. </p>
</dd>

### -param ISARanges [in]

<dd>
<p>This parameter is copied into the <b>TypeSpecificFlags</b> member of the initialized <a href="..\pepfx\ns-pepfx--pep-acpi-extended-address.md">PEP_ACPI_EXTENDED_ADDRESS</a> structure.</p>
</dd>

### -param AddressGranularity [in]

<dd>
<p>A bit mask indicating which bits have been decoded.</p>
</dd>

### -param AddressMinimum [in]

<dd>
<p>For bridges that translate addresses, this indicates the minimum starting address on the secondary side of the bridge.</p>
</dd>

### -param AddressMaximum [in]

<dd>
<p>For bridges that translate addresses, this indicates the maximum starting address on the secondary side of the bridge.</p>
</dd>

### -param AddressTranslation [in]

<dd>
<p>For bridges that translate addresses across the bridge, this is the
address on the primary side. </p>
</dd>

### -param RangeLength [in]

<dd>
<p>The length of the address range. </p>
</dd>

### -param TypeSpecificAttributes [in]

<dd>
<p>The type-specific attributes for this resource.</p>
</dd>

### -param DescriptorName [in]

<dd>
<p>The name of the resource descriptor.</p>
</dd>

### -param TranslationTypeNonStatic [in]

<dd>
<p>When true, indicates that the resource uses type translation. Otherwise, it uses type-static translation.</p>
</dd>

### -param TanslationSparseDensity [in]

<dd>
<p>When false, indicates that this is a dense translation. Otherwise, it is sparse. </p>
</dd>

### -param Resource [out]

<dd>
<p>This is cast to *<a href="..\pepfx\ns-pepfx--pep-acpi-extended-address.md">PEP_ACPI_EXTENDED_ADDRESS</a>.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\pepfx\ns-pepfx--pep-acpi-extended-address.md">PEP_ACPI_EXTENDED_ADDRESS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
