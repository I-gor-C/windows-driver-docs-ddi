---
UID : NS:ntifs._OPEN_REPARSE_LIST_ENTRY
title : _OPEN_REPARSE_LIST_ENTRY
author : windows-driver-content
description : This structure supports callers opening specific reparse points without inhibiting reparse behavior for all classes of reparse points.
old-location : ifsk\open_reparse_list_entry_.htm
old-project : ifsk
ms.assetid : A6D28F60-FA38-45EA-9E3C-D2E6F899333E
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _OPEN_REPARSE_LIST_ENTRY, *POPEN_REPARSE_LIST_ENTRY, OPEN_REPARSE_LIST_ENTRY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1607
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : OPEN_REPARSE_LIST_ENTRY
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
req.typenames : "*POPEN_REPARSE_LIST_ENTRY, OPEN_REPARSE_LIST_ENTRY"
---

# _OPEN_REPARSE_LIST_ENTRY structure
This structure supports callers opening specific reparse points without
inhibiting reparse behavior for all classes of reparse points.

## Syntax
````
typedef struct _OPEN_REPARSE_LIST_ENTRY  {
  LIST_ENTRY OpenReparseListEntry;
  ULONG      ReparseTag;
  ULONG      Flags;
  GUID       ReparseGuid;
  USHORT     Size;
  USHORT     RemainingLength;
} OPEN_REPARSE_LIST_ENTRY , *POPEN_REPARSE_LIST_ENTRY ;
````

## Members

        
            `Flags`

            Flags that control behavior when a reparse point is encountered on a directory that may be non-empty (one whose reparse tag is  recognized by <b>FsRtlIsNonEmptyDirectoryReparsePointAllowed</b>)
.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `OpenReparseListEntry`

            The entry in the open reparse list.
        
            `RemainingLength`

            The unprocessed path length when the reparse point was
    encountered.
        
            `ReparseGuid`

            The GUID of the reparse tag that should be opened directly without returning <b>STATUS_REPARSE</b>.
        
            `ReparseTag`

            The reparse tag that should be opened directly without returning <b>STATUS_REPARSE</b>.
        
            `Size`

            The size of this structure.

    ## Remarks
        This structure lets callers open specific reparse points without
  inhibiting reparse behavior for all classes of reparse points.
<a href="..\ntifs\ns-ntifs-_open_reparse_list.md">OPEN_REPARSE_LIST</a> is a structure used in an ECP with <b>ECP_TYPE_OPEN_REPARSE_GUID</b> (<code>323eb6a8-affd-4d95-8230-863bce09d37a</code>). The <b>OPEN_REPARSE_LIST</b> points to a list of <b>OPEN_REPARSE_LIST_ENTRY</b>
structures specifying the tag and possibly GUID that should be
  opened directly without returning <b>STATUS_REPARSE</b>.
If a match is found, the corresponding <b>OPEN_REPARSE_LIST_ENTRY</b>  structure will have the <b>OPEN_REPARSE_POINT_TAG_ENCOUNTERED</b> flag set to indicate that the object that was opened matched the given criteria. If a match is found for a directory that is not the final path  component and <b>STATUS_REPARSE</b> is returned, the unprocessed path
  length will be set in the <b>RemainingLength</b> field.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h |