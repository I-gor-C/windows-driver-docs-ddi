---
UID: NS.fltkernel._FLT_TAG_DATA_BUFFER
title: FLT_TAG_DATA_BUFFER
author: windows-driver-content
description: The FLT_TAG_DATA_BUFFER structure contains information about a reparse point tag.
old-location: ifsk\flt_tag_data_buffer.htm
old-project: ifsk
ms.assetid: a101e0c8-7121-42b6-aa0e-299f37af8e47
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FLT_TAG_DATA_BUFFER, FLT_TAG_DATA_BUFFER, *PFLT_TAG_DATA_BUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_TAG_DATA_BUFFER
req.alt-loc: fltkernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FLT_TAG_DATA_BUFFER structure



## -description
<p>The FLT_TAG_DATA_BUFFER structure contains information about a reparse point tag. </p>


## -syntax

````
typedef struct _FLT_TAG_DATA_BUFFER {
  ULONG  FileTag;
  USHORT TagDataLength;
  USHORT UnparsedNameLength;
  union {
    struct {
      USHORT SubstituteNameOffset;
      USHORT SubstituteNameLength;
      USHORT PrintNameOffset;
      USHORT PrintNameLength;
      ULONG  Flags;
      WCHAR  PathBuffer[1];
    } SymbolicLinkReparseBuffer;
    struct {
      USHORT SubstituteNameOffset;
      USHORT SubstituteNameLength;
      USHORT PrintNameOffset;
      USHORT PrintNameLength;
      WCHAR  PathBuffer[1];
    } MountPointReparseBuffer;
    struct {
      UCHAR DataBuffer[1];
    } GenericReparseBuffer;
    struct {
      GUID  TagGuid;
      UCHAR DataBuffer[1];
    } GenericGUIDReparseBuffer;
  };
} FLT_TAG_DATA_BUFFER, *PFLT_TAG_DATA_BUFFER;
````


## -struct-fields
<dl>

### -field FileTag

<dd>
<p>Reparse point tag. </p>
</dd>

### -field TagDataLength

<dd>
<p>Size, in bytes, of the reparse data pointed to by the <b>DataBuffer</b> member.</p>
</dd>

### -field UnparsedNameLength

<dd>
<p>Length, in bytes, of the unparsed portion of the file name pointed to by the <b>FileName</b> member of the associated file object.  For more information about the <b>FileName</b> member, see <a href="..\wdm\ns-wdm--file-object.md">FILE_OBJECT</a>.</p>
</dd>

### -field ( unnamed union )

<dd>
<p> </p>
<dl>

### -field SymbolicLinkReparseBuffer

<dd>
<dl>

### -field SubstituteNameOffset

<dd>
<p>Offset, in bytes, of the substitute name string in the <b>PathBuffer</b> array. Note that this offset must be divided by <b>sizeof(</b>WCHAR<b>)</b> to get the array index. </p>
</dd>

### -field SubstituteNameLength

<dd>
<p>Length, in bytes, of the substitute name string. If the substitute name string is NULL-terminated, <b>SubstituteNameLength</b> does not include space for the UNICODE_NULL terminator. </p>
</dd>

### -field PrintNameOffset

<dd>
<p>Offset, in bytes, of the print name string in the <b>PathBuffer</b> array. Note that this offset must be divided by <b>sizeof(</b>WCHAR<b>)</b> to get the array index. </p>
</dd>

### -field PrintNameLength

<dd>
<p>Length, in bytes, of the print name string. If the print name string is NULL-terminated, <b>PrintNameLength</b> does not include space for the UNICODE_NULL terminator. </p>
</dd>

### -field Flags

<dd>
<p>If the SYMLINK_FLAG_RELATIVE flag is set, the <b>PathBuffer</b> path is relative to the path contained in the <b>FileName</b> member of the associated file object.</p>
</dd>

### -field PathBuffer

<dd>
<p>First character of the path string. This character is followed in memory by the remainder of the string. </p>
</dd>
</dl>
</dd>

### -field MountPointReparseBuffer

<dd>
<dl>

### -field SubstituteNameOffset

<dd>
<p>Offset, in bytes, of the substitute name string in the <b>PathBuffer</b> array. Note that this offset must be divided by <b>sizeof(</b>WCHAR<b>)</b> to get the array index. </p>
</dd>

### -field SubstituteNameLength

<dd>
<p>Length, in bytes, of the substitute name string. If the substitute name string is NULL-terminated, <b>SubstituteNameLength</b> does not include space for the UNICODE_NULL terminator. </p>
</dd>

### -field PrintNameOffset

<dd>
<p>Offset, in bytes, of the print name string in the <b>PathBuffer</b> array. Note that this offset must be divided by <b>sizeof(</b>WCHAR<b>)</b> to get the array index. </p>
</dd>

### -field PrintNameLength

<dd>
<p>Length, in bytes, of the print name string. If the print name string is NULL-terminated, <b>PrintNameLength</b> does not include space for the UNICODE_NULL terminator. </p>
</dd>

### -field PathBuffer

<dd>
<p>First character of the path string. This character is followed in memory by the remainder of the string. </p>
</dd>
</dl>
</dd>

### -field GenericReparseBuffer

<dd>
<dl>

### -field DataBuffer

<dd>
<p>Pointer to a buffer that contains user-defined data for the reparse point. </p>
</dd>
</dl>
</dd>

### -field GenericGUIDReparseBuffer

<dd>
<dl>

### -field TagGuid

<dd>
<p>Globally unique identifier (GUID) that uniquely identifies the type of reparse point. If <b>FileTag</b> is not a Microsoft tag, this member cannot be <b>NULL</b>. </p>
</dd>

### -field DataBuffer

<dd>
<p>Pointer to a buffer that contains user-defined data for the reparse point. </p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>A minifilter can use the FLT_TAG_DATA_BUFFER structure to store information about a reparse point tag. </p>

<p>A pointer to an FLT_TAG_DATA_BUFFER structure that contains reparse point tag data for an operation is stored in the <b>TagData</b> member of the <a href="..\fltkernel\ns-fltkernel--flt-callback-data.md">FLT_CALLBACK_DATA</a> structure for the operation. </p>

<p>The FLT_TAG_DATA_BUFFER_HEADER_SIZE macro returns the size of the fixed portion of the FLT_TAG_DATA_BUFFER structure. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include FltKernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--file-object.md">FILE_OBJECT</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-callback-data.md">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-flttagfile.md">FltTagFile</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltuntagfile.md">FltUntagFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_TAG_DATA_BUFFER structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
