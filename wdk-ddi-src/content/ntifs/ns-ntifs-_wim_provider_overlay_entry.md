---
UID : NS:ntifs._WIM_PROVIDER_OVERLAY_ENTRY
title : _WIM_PROVIDER_OVERLAY_ENTRY
author : windows-driver-content
description : Contains the a Windows Image Format (WIM) file configuration information for a data source entry. It is used to identify specific WIM file names and indices that supply data to externally backed files on a volume.
old-location : ifsk\wim_provider_overlay_entry.htm
old-project : ifsk
ms.assetid : 8D1C9C8B-0545-42D7-860F-E2263457E61F
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _WIM_PROVIDER_OVERLAY_ENTRY, *PWIM_PROVIDER_OVERLAY_ENTRY, WIM_PROVIDER_OVERLAY_ENTRY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : Ntifs.h, Fltkernel.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows 8.1 Update.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WIM_PROVIDER_OVERLAY_ENTRY
req.alt-loc : ntifs.h
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
req.typenames : "*PWIM_PROVIDER_OVERLAY_ENTRY, WIM_PROVIDER_OVERLAY_ENTRY"
---

# _WIM_PROVIDER_OVERLAY_ENTRY structure
Contains the  a Windows Image Format (WIM) file configuration information for a data source entry. It is used to identify specific WIM file names and indices that supply data to externally backed files on a volume.

## Syntax
````
typedef struct _WIM_PROVIDER_OVERLAY_ENTRY {
  ULONG         NextEntryOffset;
  LARGE_INTEGER DataSourceId;
  GUID          WimGuid;
  ULONG         WimFileNameOffset;
  ULONG         WimType;
  ULONG         WimIndex;
  ULONG         Flags;
} WIM_PROVIDER_OVERLAY_ENTRY, *PWIM_PROVIDER_OVERLAY_ENTRY;
````

## Members

        
            `DataSourceId`

            The specific identifier an overlay entry. A single WIM GUID, such as in the <b>WimGuid</b> member, may have multiple  data source identifiers.
        
            `Flags`

            The status flags for the WIM provider. Set to 0 when active. Otherwise <b>Flags</b> is set to one of the following values.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `NextEntryOffset`

            The offset to the next WIM_PROVIDER_OVERLAY_ENTRY structure returned in the enumeration. Set to 0 if there are no further entries.
        
            `WimFileNameOffset`

            The offset, in bytes, from the beginning of this structure of the file name for the WIM file to add as a backing source. The file name is a NULL terminated string of <b>WCHAR</b> character values.
        
            `WimGuid`

            A unique identifier of a WIM file.
        
            `WimIndex`

            The index of the image in the WIM file specified at <b>WimFileNameOffset</b>.
        
            `WimType`

            The type of WIM file set as a backing source. The WIM file type is set to one of the following values.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn632440">FSCTL_ENUM_OVERLAY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20WIM_PROVIDER_OVERLAY_ENTRY structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>